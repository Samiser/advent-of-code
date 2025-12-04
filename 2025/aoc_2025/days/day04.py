def reachable(diagram: list[list[str]], center_x: int, center_y: int) -> int:
    count = 0

    for y in range(center_y - 1, center_y + 2):
        for x in range(center_x - 1, center_x + 2):
            if x >= 0 and x < len(diagram) and y >= 0 and y < len(diagram[0]):
                if diagram[y][x] == "@":
                    count += 1

    return count - 1 < 4


def remove_rolls(diagram: list[list[str]]) -> tuple[int, list[list[str]]]:
    paper = 0
    illustration: list[list[str]] = [row[:] for row in diagram]

    for y in range(len(diagram)):
        for x in range(len(diagram[0])):
            if diagram[y][x] == "@" and reachable(diagram, x, y):
                paper += 1
                illustration[y][x] = "x"

    return paper, illustration


def part1(data: str) -> str:
    diagram: list[list[str]] = [list(line) for line in data.splitlines()]
    count, _new_diagram = remove_rolls(diagram)
    return str(count)


def part2(data: str) -> str:
    total_removed = 0
    removed_count = 0
    diagram: list[list[str]] = [list(line) for line in data.splitlines()]

    (removed_count, diagram) = remove_rolls(diagram)

    while removed_count > 0:
        total_removed += removed_count
        (removed_count, diagram) = remove_rolls(diagram)

    return str(total_removed)
