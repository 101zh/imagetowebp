import argparse
from imagetowebp.convert import convert_to_webp
from pathlib import Path
from PIL import UnidentifiedImageError

parser = argparse.ArgumentParser(
    description="A cli tool that converts images to .webp files"
)
parser.add_argument("input_path", help="The file path of image to be converted")
parser.add_argument(
    "-output-path", "-o", help="The output folder or file path for converted file", default=None
)


def main() -> None:
    args = parser.parse_args()

    try:
        convert_to_webp(args.input_path, args.output_path)
    except Exception as e:
        print(e)
