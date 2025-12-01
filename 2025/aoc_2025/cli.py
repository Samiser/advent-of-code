import argparse
from pathlib import Path
from dataclasses import dataclass

from . import days
from . import inputs


@dataclass
class Args:
    day: int
    part: int
    inputs: Path


def main() -> None:
    parser = argparse.ArgumentParser()
    _ = parser.add_argument("day", type=int)
    _ = parser.add_argument(
        "-i",
        "--inputs",
        type=Path,
        default=Path("inputs"),
        help="path to the input files directory",
    )

    args = parser.parse_args(namespace=Args)

    try:
        module = days.load(args.day)
        data = inputs.load(args.day, args.inputs)
    except ValueError as e:
        parser.error(str(e))

    print(module.part1(data))
    print(module.part2(data))
