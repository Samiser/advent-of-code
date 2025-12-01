def rotate(current_position: int, instruction: str) -> int:
    direction = instruction[:1]
    count = int(instruction[1:])

    if direction == "L":
        count *= -1

    return (current_position + count) % 100


def part1(data: str) -> str:
    position = 50
    zero_count = 0

    for instruction in data.splitlines():
        position = rotate(position, instruction)
        if position == 0:
            zero_count += 1

    return str(zero_count)


def part2(data: str) -> str:
    return "todo!"
