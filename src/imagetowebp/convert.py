from PIL import Image
from pathlib import Path
from imagetowebp.exceptions import InvalidPathError


def convert_to_webp(img_path: str, output_path: str) -> None:

    if not Path(img_path).exists():
        raise InvalidPathError(f'Input Image: "{img_path}" does not exist')

    out: Path = create_output_path(img_path, output_path)

    with Image.open(img_path) as im:

        shouldSaveAllFrames: bool = (
            getattr(im, "is_animated", False) and im.info.get("duration") != None
        )

        try:
            im.save(out, format="webp", save_all=shouldSaveAllFrames)
        except FileNotFoundError:
            raise InvalidPathError(f'Output Path: "{output_path}" does not exist')


def create_output_path(input_path: str, output_path: str) -> Path:
    if output_path == None:
        output_path = input_path

    out: Path = Path(output_path)

    if out.suffix == None or out.suffix == "":
        out = out.joinpath(Path(input_path).name)

    return out.with_suffix(".webp")
