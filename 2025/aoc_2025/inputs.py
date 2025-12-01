from pathlib import Path


def load(day: int, inputs_dir: Path) -> str:
    path = inputs_dir / f"day{day:02d}.txt"
    try:
        return path.read_text().rstrip("\n")
    except FileNotFoundError:
        raise ValueError(f"no input file found at {path}")
