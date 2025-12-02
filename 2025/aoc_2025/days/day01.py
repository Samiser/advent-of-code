def count_zero_passes(current_position: int, rotation: int) -> int:
    if rotation < 0:
        current_position = -current_position % 100
        rotation = -rotation

    return (current_position + rotation) // 100


def day1(data: str) -> tuple[int, int]:
    position = 50
    p1_count = 0
    p2_count = 0

    rotations = [
        int(line[1:]) * (1 if line[:1] == "R" else -1) for line in data.splitlines()
    ]
    for rotation in rotations:
        p2_count += count_zero_passes(position, rotation)
        position = (position + rotation) % 100
        if position == 0:
            p1_count += 1

    return p1_count, p2_count


def part1(data: str) -> str:
    return str(day1(data)[0])


def part2(data: str) -> str:
    return str(day1(data)[1])
