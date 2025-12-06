import math


def calculate(value_lines: list[list[int]], operators: list[str]) -> int:
    total = 0
    for values, operator in zip(value_lines, operators):
        if operator == "+":
            total += sum(values)
        elif operator == "*":
            total += math.prod(values)
    return total


def part1(lines: list[str], operators: list[str]) -> int:
    rows: list[list[int]] = [[int(val) for val in line.split()] for line in lines]

    value_lines: list[list[int]] = [list(line) for line in zip(*reversed(rows))]

    return calculate(value_lines, operators)


def part2(lines: list[str], operators: list[str]) -> int:
    matrix: list[list[str]] = [list(line) for line in lines]

    value_lines: list[list[int]] = []
    current: list[int] = []

    for row in zip(*reversed(matrix)):
        line: list[str] = list(row)[::-1]
        if all([ch == " " for ch in line]):
            value_lines.append(current)
            current = []
        else:
            current.append(int("".join(line)))
    value_lines.append(current)

    return calculate(value_lines, operators)


def solve(data: str) -> tuple[int, int]:
    lines = data.splitlines()
    operators = lines[-1].split()
    value_lines = lines[:-1]

    return part1(value_lines, operators), part2(value_lines, operators)
