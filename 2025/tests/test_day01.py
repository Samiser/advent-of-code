from aoc_2025.days.day01 import part1, part2, count_zero_passes

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


def test_part2_edge() -> None:
    # testing edge cases to ensure double-counting zeros is avoided

    # rotation left to 0 should count as 1
    assert count_zero_passes(50, -50) == 1
    # rotation left from 0 should count as 0
    assert count_zero_passes(0, 50) == 0
