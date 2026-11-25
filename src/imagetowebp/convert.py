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
    out: Path = create_dir_output_path(folder_path, output_path)

    files = folder_path.glob("*")

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures: list[Future] = []

        for file in files:
            if file.is_file():  # Only processes files inside a folder
                # Tells executor to run a thread to process a file and add that thread to a list of threads
                futures.append(
                    executor.submit(process_file, file, out, quality, is_lossless)
                )

        # Waits for all file conversion to be completed before ending function
        # by checking if all threads in the list have been completed
        for future in as_completed(futures):
            future.result()


def process_file(file: Path, out: Path, quality: int, is_lossless: bool) -> None:
    try:
        convert_file(
            file,
            out.joinpath(file.name).with_suffix(".webp"),
            quality,
            is_lossless,
        )
    except UnidentifiedImageError:
        print(f'"{file}" cannot be identified as an image, it is being ignored')


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
