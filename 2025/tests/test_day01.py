from aoc_2025.days.day01 import solve, count_zero_passes

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
    assert solve(input.strip())[0] == 3


def test_part2() -> None:
    assert solve(input.strip())[1] == 6


def test_part2_edge() -> None:
    # testing edge cases to ensure double-counting zeros is avoided

    # rotation left to 0 should count as 1
    assert count_zero_passes(50, -50) == 1
    # rotation left from 0 should count as 0
    assert count_zero_passes(0, 50) == 0
