def solve(data: str) -> tuple[int, int]:
    lines = data.splitlines()

    beam_positions: set[int] = set()
    split_count = 0
    timeline_counts = [0] * len(lines[0])

    beam_positions.add(lines[0].find("S"))

    for line in lines:
        for pos, char in enumerate(line):
            if char == "^" and pos in beam_positions:
                split_count += 1
                beam_positions.add(pos - 1)
                beam_positions.add(pos + 1)
                beam_positions.remove(pos)

                count = timeline_counts[pos]
                timeline_counts[pos - 1] += count if count > 0 else 1
                timeline_counts[pos + 1] += count if count > 0 else 1
                timeline_counts[pos] = 0

    return split_count, sum(timeline_counts)
