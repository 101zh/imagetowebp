import argparse
from imagetowebp.convert import convert_to_webp, convert_directory
from PIL import UnidentifiedImageError
from imagetowebp.exceptions import InvalidPathError, IllegalArgumentError
from pathlib import Path

parser = argparse.ArgumentParser(
    description="A cli tool that converts images to .webp files"
)
parser.add_argument("input_path", help="The file/folder path of image(s) to be converted")
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


def main() -> None:
    args = parser.parse_args()

    try:
        img_path: Path = validate_input_path(args.input_path)
        quality: int = validate_quality_arg(args.quality)

        if img_path.is_dir():
            convert_directory(img_path, args.output_path, quality, args.lossless)
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
