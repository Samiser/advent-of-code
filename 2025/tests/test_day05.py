from aoc_2025.days.day05 import part1, part2

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
    assert part1(input.strip()) == "3"


def test_part2() -> None:
    assert part2(input.strip()) == "14"
