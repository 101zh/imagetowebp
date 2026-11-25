import argparse
from imagetowebp.convert import convert_to_webp, convert_directory
from PIL import UnidentifiedImageError
from imagetowebp.exceptions import InvalidPathError, IllegalArgumentError
from pathlib import Path
import os

parser = argparse.ArgumentParser(
    description="A cli tool that converts images to .webp files"
)
parser.add_argument(
    "input_path", help="The file/folder path of image(s) to be converted"
)
parser.add_argument(
    "-o",
    "--output-path",
    help="The output file/folder path for converted file(s)",
    default=None,
)
parser.add_argument(
    "-q",
    "--quality",
    help="""An integer (0-100), default 80. Lower values produce 
        smaller files; higher values produce larger files. In 
        --lossless mode, 0 minimizes compression effort (larger 
        files), while 100 maximizes it (smaller files).""",
    default=80,
)
parser.add_argument(
    "-l",
    "--lossless",
    help="If used, saves the webp using lossless compression",
    action="store_true",
    default=False,
)
parser.add_argument(
    "-t",
    "--threads",
    help="""The max number of worker threads when processing a 
    directory of files. This flag is ignored when processing 
    singular image files. By default it is 8 or the number of 
    cpu cores subtracted by 2""",
    default=None,
)


def main() -> None:
    args = parser.parse_args()

    try:
        img_path: Path = validate_input_path(args.input_path)
        quality: int = validate_quality_arg(args.quality)
        threads: int = validate_threads_arg(args.threads)

        if img_path.is_dir():
            convert_directory(
                img_path, args.output_path, quality, args.lossless, threads
            )
        else:
            convert_to_webp(img_path, args.output_path, quality, args.lossless)

        print("All Done!")
    except UnidentifiedImageError:
        print(f'File: "{args.input_path}" cannot be identified as an image')
    except InvalidPathError as e:
        print(e)
    except IllegalArgumentError as e:
        print(e)


def validate_quality_arg(quality_arg: str) -> int:
    try:
        quality = int(quality_arg)

        if quality < 0 or quality > 100:
            raise IllegalArgumentError(
                f'"{quality_arg}" is not a valid number for quality'
            )

        return quality
    except ValueError:
        raise IllegalArgumentError(
            f'"{quality_arg}" is not a whole number for the quality parameter'
        )


def validate_input_path(input_path: str) -> Path:
    img_path: Path = Path(input_path)

    if not img_path.exists():
        raise InvalidPathError(f'Input file/directory: "{input_path}" does not exist')

    return img_path


def validate_threads_arg(threads_arg: str) -> int:
    try:
        threads: int

        if threads_arg == None:
            # if cpu_count can't be retrieved then use 8 threads.
            # if cpu_count can be retrieved then attempt to use
            # the cpu_count - 2 number of threads unless the computer has 2 cores or less.
            threads = 8 if os.cpu_count() == None else max(1, os.cpu_count() - 2)
        else:
            threads = int(threads_arg)

        if threads <= 0 or threads > 61:
            raise IllegalArgumentError(
                f'"{threads_arg}" is not a valid number for threads'
            )

        return threads
    except ValueError:
        raise IllegalArgumentError(
            f'"{threads_arg}" is not a whole number for the threads parameter'
        )
