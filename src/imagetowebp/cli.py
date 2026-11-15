import argparse

parser = argparse.ArgumentParser(
    description="An cli tool that converts images to .webp files")
parser.add_argument("path", help="The file path to the image to be converted")
parser.add_argument("-output-path", "-o",
                    help="The output file path of the .webp file")


def main() -> None:
    args = parser.parse_args()
    print(args.path)
    print(args.output_path)
