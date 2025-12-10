from aoc_2025.days.day09 import solve

input = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""


def test_part1() -> None:
    assert solve(input.strip())[0] == 50


def test_part2() -> None:
    assert solve(input.strip())[1] == 24
