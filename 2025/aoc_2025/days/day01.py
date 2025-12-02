def parse_instruction(instruction: str) -> int:
    return int(instruction[1:]) * (1 if instruction[:1] == "R" else -1)


def rotate(current_position: int, instruction: str) -> int:
    rotation = parse_instruction(instruction)

    return (current_position + rotation) % 100


def count_zero_passes(current_position: int, instruction: str) -> int:
    rotation = parse_instruction(instruction)

    if rotation >= 0:
        return (current_position + rotation) // 100

    hit = current_position if current_position > 0 else 100

    if abs(rotation) < hit:
        return 0

    return 1 + (abs(rotation) - hit) // 100


def part1(data: str) -> str:
    position = 50
    zero_count = 0

    for instruction in data.splitlines():
        position = rotate(position, instruction)
        if position == 0:
            zero_count += 1

    return str(zero_count)


def part2(data: str) -> str:
    position = 50
    zero_passes = 0

    for instruction in data.splitlines():
        zero_passes += count_zero_passes(position, instruction)
        position = rotate(position, instruction)

    return str(zero_passes)
