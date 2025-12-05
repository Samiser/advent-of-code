from aoc_2025.days.day05 import solve

input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def test_part1() -> None:
    assert solve(input.strip())[0] == 3


def test_part2() -> None:
    assert solve(input.strip())[1] == 14
