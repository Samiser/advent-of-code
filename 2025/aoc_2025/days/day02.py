from typing import Callable

IdValidator = Callable[[str], bool]


def is_repeated_block(str_id: str, size: int) -> bool:
    length = len(str_id)
    if length % size != 0:
        return False

    block = str_id[:size]
    return block * (length // size) == str_id


def count_invalid(data: str, is_invalid: IdValidator):
    total = 0

    for start, end in (s.split("-") for s in data.split(",")):
        for id in range(int(start), int(end) + 1):
            if is_invalid(str(id)):
                total += id

    return str(total)


def part1(data: str) -> str:
    def has_pair(id: str) -> bool:
        return len(id) % 2 == 0 and is_repeated_block(id, len(id) // 2)

    return count_invalid(data, has_pair)


def part2(data: str) -> str:
    def has_any_repeated_block(id: str) -> bool:
        return any(is_repeated_block(id, size) for size in range(1, len(id)))

    return count_invalid(data, has_any_repeated_block)
