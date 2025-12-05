Diagram = list[list[str]]


def reachable(diagram: Diagram, center_x: int, center_y: int) -> int:
    height = len(diagram)
    width = len(diagram[0])

    neighbours = sum(
        1
        for y in range(center_y - 1, center_y + 2)
        for x in range(center_x - 1, center_x + 2)
        if 0 <= x < width
        and 0 <= y < height
        and not (x == center_x and y == center_y)
        and diagram[y][x] == "@"
    )

    return neighbours < 4


def remove_rolls(diagram: Diagram) -> tuple[int, Diagram]:
    paper = 0
    illustration: Diagram = [row[:] for row in diagram]

    height = len(diagram)
    width = len(diagram[0])

    for y in range(height):
        for x in range(width):
            if diagram[y][x] == "@" and reachable(diagram, x, y):
                paper += 1
                illustration[y][x] = "x"

    return paper, illustration


def solve(data: str) -> tuple[int, int]:
    total_removed = 0
    first_removed, diagram = remove_rolls([list(line) for line in data.splitlines()])

    removed_count = first_removed

    while removed_count:
        total_removed += removed_count
        removed_count, diagram = remove_rolls(diagram)

    return first_removed, total_removed
