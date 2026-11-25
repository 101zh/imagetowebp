import argparse
from imagetowebp.convert import convert_to_webp
from PIL import UnidentifiedImageError
from imagetowebp.exceptions import InvalidPathError, IllegalArgumentError

parser = argparse.ArgumentParser(
    description="A cli tool that converts images to .webp files"
)
parser.add_argument("input_path", help="The file path of image to be converted")
parser.add_argument(
    "-o",
    "--output-path",
    help="The output folder or file path for converted file",
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
        convert_to_webp(args.input_path, args.output_path, args.quality, args.lossless)
    except UnidentifiedImageError:
        print(f'File: "{args.input_path}" cannot be identified as an image')
    except InvalidPathError as e:
        print(e)
    except IllegalArgumentError as e:
        print(e)
