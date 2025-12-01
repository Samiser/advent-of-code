import textwrap
from aoc_2025.days.day01 import part1


def test_part1() -> None:
    input = textwrap.dedent(
        """\
        L68
        L30
        R48
        L5
        R60
        L55
        L1
        L99
        R14
        L82"""
    )

    assert part1(input.strip()) == 3
