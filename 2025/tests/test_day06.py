from aoc_2025.days.day06 import solve

input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """


def test_part1() -> None:
    assert solve(input.strip())[0] == 4277556


def test_part2() -> None:
    assert solve(input.strip())[1] == 3263827
