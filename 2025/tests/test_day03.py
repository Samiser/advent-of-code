from aoc_2025.days.day03 import part1, part2

input = """987654321111111
811111111111119
234234234234278
818181911112111"""


def test_part1() -> None:
    assert part1(input.strip()) == "357"


def test_part2() -> None:
    assert part2(input.strip()) == "3121910778619"
