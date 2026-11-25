from PIL import Image
from pathlib import Path
from imagetowebp.exceptions import InvalidPathError, IllegalArgumentError


def convert_to_webp(
    img_path: str, output_path: str, quality_arg: str, is_lossless: bool
) -> None:

    try:
        quality = int(quality_arg)
        if quality < 0 or quality > 100:
            raise IllegalArgumentError(
                f'"{quality_arg}" is not a valid number for quality'
            )
    except ValueError:
        raise IllegalArgumentError(
            f'"{quality_arg}" is not a whole number for the quality parameter'
        )

    if not Path(img_path).exists():
        raise InvalidPathError(f'Input Image: "{img_path}" does not exist')

    out: Path = create_output_path(img_path, output_path)

    with Image.open(img_path) as im:

        shouldSaveAllFrames: bool = (
            getattr(im, "is_animated", False) and im.info.get("duration") != None
        )

        try:
            im.save(
                out,
                format="webp",
                save_all=shouldSaveAllFrames,
                quality=quality,
                lossless=is_lossless,
            )
        except FileNotFoundError:
            raise InvalidPathError(f'Output Path: "{output_path}" does not exist')


def create_output_path(input_path: str, output_path: str) -> Path:
    if output_path == None:
        # If no output path is supplied the output will be in the same directory as the input
        output_path = input_path

    out: Path = Path(output_path)

    # If no file name is provided in the output path, use the name of the original file
    if out.suffix == None or out.suffix == "":
        out = out.joinpath(Path(input_path).name)

    return out.with_suffix(".webp")
