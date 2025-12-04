def joltage(bank: list[int], count: int) -> int:
    chosen: list[int] = []
    max_pos = 0

    for i in range(count):
        candidates = range(max_pos + int(i > 0), len(bank) - (count - i - 1))
        max_pos = max(candidates, key=bank.__getitem__)
        chosen.append(bank[max_pos])

    return int("".join([str(digit) for digit in chosen]))


def banks_to_joltages(banks: list[str], size: int):
    return [joltage([int(x) for x in line], size) for line in banks]


def solve(data: str, size: int):
    return str(sum(banks_to_joltages(data.splitlines(), size)))


def part1(data: str) -> str:
    return solve(data, 2)


def part2(data: str) -> str:
    return solve(data, 12)
