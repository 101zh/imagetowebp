from typing import Iterator
from PIL import Image, UnidentifiedImageError
from pathlib import Path
from imagetowebp.exceptions import InvalidPathError
from concurrent.futures import Future, ThreadPoolExecutor, as_completed


def convert_to_webp(
    img_path: Path, output_path: str, quality: int, is_lossless: bool
) -> None:

    out: Path = create_file_output_path(img_path, output_path)

    if not out.parent.exists():
        raise InvalidPathError(f'"{out.parent}" does not exist')

    convert_file(img_path, out, quality, is_lossless)


def convert_file(img_path: Path, out: Path, quality: int, is_lossless: bool) -> None:
    with Image.open(img_path) as im:

        shouldSaveAllFrames: bool = (
            getattr(im, "is_animated", False) and im.info.get("duration") != None
        )

        print(f'Working on "{img_path}"')
        im.save(
            out,
            format="webp",
            save_all=shouldSaveAllFrames,
            quality=quality,
            lossless=is_lossless,
        )
        print(f'Finished converting "{img_path}"')


def create_file_output_path(input_path: Path, output_path: str) -> Path:
    if output_path == None:
        # If no output path is supplied the output will be in the same directory as the input
        output_path = input_path

    out: Path = Path(output_path)

    # If no file name is provided in the output path, use the name of the original file
    if out.suffix == None or out.suffix == "":
        out = out.joinpath(input_path.name)

    return out.with_suffix(".webp")


def convert_directory(
    folder_path: Path, output_path: str, quality: int, is_lossless: bool, threads: int
) -> None:
    out_dir: Path = create_dir_output_path(folder_path, output_path)

    files = folder_path.glob("*")

    source_file_paths, file_paths_to_write = determine_files_to_write(files, out_dir)

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures: list[Future] = []

        for i in range(len(file_paths_to_write)):
            # Tells executor to run a thread to process a file and add that thread to a list of threads
            futures.append(
                executor.submit(
                    process_file_in_directory,
                    source_file_paths[i],
                    file_paths_to_write[i],
                    quality,
                    is_lossless,
                )
            )

        # Waits for all file conversion to be completed before ending function
        # by checking if all threads in the list have been completed
        for future in as_completed(futures):
            future.result()


def determine_files_to_write(
    files: Iterator[Path], out_dir: Path
) -> tuple[list[Path], list[Path]]:
    # The paths to each of the files that need to be processed
    source_file_paths: list[Path] = []
    # The output paths for each image file after its been processed
    file_paths_to_write: list[Path] = []
    # A hashset which keeps track of what file stems have been used
    written_filenames: set[str] = set()

    for file in files:
        # Omits folders, since they aren't files
        if file.is_file():
            source_file_paths.append(file)
            if file.stem in written_filenames:
                # If the same file stem has already been used, then use the entire file name as the file stem
                # EX: example.png -> example.png.webp if another image like example.jpg exists
                file = out_dir.joinpath(f"{file.name}.webp")
                file_paths_to_write.append(file)
                written_filenames.add(file.stem)
            else:
                written_filenames.add(file.stem)
                file_paths_to_write.append(
                    out_dir.joinpath(file.with_suffix(".webp").name)
                )

    return source_file_paths, file_paths_to_write


def process_file_in_directory(
    file: Path, out: Path, quality: int, is_lossless: bool
) -> None:
    try:
        convert_file(
            file,
            out,
            quality,
            is_lossless,
        )
    except UnidentifiedImageError:
        print(f'"{file}" cannot be identified as an image, it is being ignored')
    except ValueError as e:
        print(f'ERROR: "{file}"; {e}')
    except OSError as e:
        print(f'ERROR: "{file}"; {e}')


def create_dir_output_path(folder_path: Path, output_path: str) -> Path:
    if output_path == None:
        # If no output path is supplied the output will be in the same directory as the input
        output_path = folder_path

    out: Path = Path(output_path)

    isFolder: bool = out.suffix == None or out.suffix == ""
    if not isFolder:
        raise InvalidPathError(
            f'"{output_path}" cannot be a file when converting a directory of images'
        )

    if not out.exists():
        raise InvalidPathError(f'"{output_path} does not exist"')

    return out
