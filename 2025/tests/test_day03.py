from aoc_2025.days.day03 import solve

input = """987654321111111
811111111111119
234234234234278
818181911112111"""


def test_part1() -> None:
    assert solve(input.strip())[0] == 357


def test_part2() -> None:
    assert solve(input.strip())[1] == 3121910778619
