from bisect import bisect_right


def day5(data: str) -> tuple[str, str]:
    raw_id_ranges, raw_ids = [section.splitlines() for section in data.split("\n\n")]
    count = 0

    ids = [int(id) for id in raw_ids]
    id_ranges = [
        range(int(start), int(end) + 1)
        for start, end in (line.split("-") for line in raw_id_ranges)
    ]

    id_ranges.sort(key=lambda r: r.start)

    merged: list[range] = []
    for r in id_ranges:
        if merged and merged[-1].stop >= r.start:
            merged[-1] = range(merged[-1].start, max(merged[-1].stop, r.stop))
        else:
            merged.append(r)

    for id in ids:
        pos = bisect_right(merged, id, key=lambda r: r.start) - 1
        if pos >= 0 and id in merged[pos]:
            count += 1

    id_count: int = sum(len(r) for r in merged)

    return str(count), str(id_count)


def part1(data: str) -> str:
    return day5(data)[0]


def part2(data: str) -> str:
    return day5(data)[1]
