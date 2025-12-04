from aoc_2025.days.day04 import part1, part2

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
    assert part1(input.strip()) == "13"


def test_part2() -> None:
    assert part2(input.strip()) == "43"
