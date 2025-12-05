from aoc_2025.days.day04 import solve

input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


def test_part1() -> None:
    assert solve(input.strip())[0] == 13


def test_part2() -> None:
    assert solve(input.strip())[1] == 43
