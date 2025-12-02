import textwrap
from itertools import groupby


def get_invalid_ids(start: int, end: int) -> list[int]:
    invalid: list[int] = []
    for id in range(start, end + 1):
        str_id = str(id)
        if (
            len(str_id) % 2 == 0
            and str_id[: len(str_id) // 2] == str_id[len(str_id) // 2 :]
        ):
            invalid.append(id)
    return invalid


def get_invalid_ids_2(start: int, end: int) -> list[int]:
    invalid: list[int] = []
    for id in range(start, end + 1):
        str_id = str(id)
        for i in range(1, len(str_id)):
            if len(str_id) % i == 0:
                groups = [int(x) for x in textwrap.wrap(str_id, i)]
                grouped = groupby(groups, int)
                if len(list(grouped)) <= 1:
                    invalid.append(id)
                    break
    return invalid


def part1(data: str) -> str:
    total = 0

    for start, end in [s.split("-") for s in data.split(",")]:
        total += sum(get_invalid_ids(int(start), int(end)))

    return str(total)


def part2(data: str) -> str:
    total = 0

    for start, end in [s.split("-") for s in data.split(",")]:
        total += sum(get_invalid_ids_2(int(start), int(end)))

    return str(total)
