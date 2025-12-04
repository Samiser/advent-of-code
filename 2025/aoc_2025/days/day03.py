def boop2(bank: list[int], count: int) -> int:
    values: list[int] = []
    max_pos = max(range(len(bank) - (count - 1)), key=bank.__getitem__)
    values.append(bank[max_pos])

    for i in range(count - 1):
        cut = (count - i) - 2
        candidates = range(max_pos + 1, len(bank) - cut)
        max_pos = max(candidates, key=bank.__getitem__)
        values.append(bank[max(candidates, key=bank.__getitem__)])

    return int("".join([str(digit) for digit in values]))


def part1(data: str) -> str:
    return str(
        sum([boop2([int(x) for x in list(line)], 2) for line in data.splitlines()])
    )


def part2(data: str) -> str:
    return str(
        sum([boop2([int(x) for x in list(line)], 12) for line in data.splitlines()])
    )
