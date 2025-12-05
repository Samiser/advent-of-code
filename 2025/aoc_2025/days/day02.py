def has_pair(s: str) -> bool:
    length = len(s)
    if length % 2 != 0:
        return False
    half = length // 2
    return s[:half] == s[half:]


def has_any_repeated_block(s: str) -> bool:
    length = len(s)
    limit = length // 2
    for size in range(1, limit + 1):
        if length % size != 0:
            continue
        block = s[:size]
        if block * (length // size) == s:
            return True
    return False


def count_invalid(data: str) -> tuple[str, str]:
    pair_total = 0
    repeated_block_total = 0

    for start, end in (s.split("-") for s in data.split(",")):
        for n in range(int(start), int(end) + 1):
            s = str(n)
            if has_pair(s):
                pair_total += n
                repeated_block_total += n
                continue
            if has_any_repeated_block(s):
                repeated_block_total += n

    return str(pair_total), str(repeated_block_total)


def part1(data: str) -> str:
    return count_invalid(data)[0]


def part2(data: str) -> str:
    return count_invalid(data)[1]


def solve(data: str) -> str:
    return "\n".join(count_invalid(data))
