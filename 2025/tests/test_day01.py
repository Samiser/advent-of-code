from aoc_2025.days.day01 import part1, part2

input = """\
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


def test_part1() -> None:
    assert part1(input.strip()) == "3"


def test_part2() -> None:
    assert part2(input.strip()) == "6"
