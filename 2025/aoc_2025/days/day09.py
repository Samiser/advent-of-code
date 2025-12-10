from collections.abc import Iterator, Iterable, Callable
from collections import deque
from itertools import combinations
from typing import cast

Point = tuple[int, int]
Box = tuple[Point, Point]


def build_border(coords: list[Point]) -> set[Point]:
    n = len(coords)
    boundary: set[Point] = set()

    for i in range(n):
        x1, y1 = coords[i]
        x2, y2 = coords[(i + 1) % n]

        if x1 == x2:
            step = 1 if y2 >= y1 else -1
            for y in range(y1, y2 + step, step):
                boundary.add((x1, y))
        elif y1 == y2:
            step = 1 if x2 >= x1 else -1
            for x in range(x1, x2 + step, step):
                boundary.add((x, y1))

    return boundary


def flood_fill_outside(boundary: set[Point], max_x: int, max_y: int) -> set[Point]:
    outside: set[Point] = set()
    q: deque[Point] = deque()

    for x in range(-1, max_x + 2):
        q.append((x, -1))
        q.append((x, max_y + 1))
    for y in range(0, max_y + 1):
        q.append((-1, y))
        q.append((max_x + 1, y))

    def neighbors(p: Point):
        x, y = p
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            yield nx, ny

    while q:
        p = q.popleft()
        if p in outside or p in boundary:
            continue
        x, y = p
        if x < -1 or x > max_x + 1 or y < -1 or y > max_y + 1:
            continue
        outside.add(p)
        for np in neighbors(p):
            if np not in outside and np not in boundary:
                q.append(np)

    return outside


def get_inside_tiles(
    boundary: set[Point], outside: set[Point], max_x: int, max_y: int
) -> set[Point]:
    inside: set[Point] = set(boundary)

    for x in range(0, max_x + 1):
        for y in range(0, max_y + 1):
            if (x, y) not in outside:
                inside.add((x, y))

    return inside


def build_valid(points: list[Point]) -> set[Point]:
    max_x = max(x for x, _y in points)
    max_y = max(y for _x, y in points)

    boundary = build_border(points)
    outside = flood_fill_outside(boundary, max_x, max_y)

    return get_inside_tiles(boundary, outside, max_x, max_y)


def size(p: Box) -> int:
    (x1, y1), (x2, y2) = p
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def compress(values: list[int]) -> tuple[list[int], Callable[[list[int]], list[int]]]:
    map_to: dict[int, int] = {}
    map_from: dict[int, int] = {}

    for i, val in enumerate(sorted(values[::2])):
        map_to[val] = i
        map_from[i] = val

    mapped = [map_to[val] for val in values]

    def decompress(values: list[int]) -> list[int]:
        return [map_from[val] for val in values]

    return mapped, decompress


def compress_2d(
    values: list[Point],
) -> tuple[
    list[Point],
    Callable[[Iterable[Point]], Iterable[Point]],
]:
    xs = list([x for x, _y in values])
    ys = list([y for _x, y in values])

    x, x_dec = compress(xs)
    y, y_dec = compress(ys)

    def decompress(values: Iterable[Point]) -> Iterable[Point]:
        xs = list([x for x, _y in values])
        ys = list([y for _x, y in values])
        return list(zip(x_dec(xs), y_dec(ys)))

    return list(zip(x, y)), decompress


def rect_border_points(box: Box) -> Iterator[Point]:
    x1, y1 = box[0]
    x2, y2 = box[1]
    xmin, xmax = sorted((x1, x2))
    ymin, ymax = sorted((y1, y2))

    for x in range(xmin, xmax + 1):
        yield (x, ymin)
        if ymax != ymin:
            yield (x, ymax)

    for y in range(ymin + 1, ymax):
        yield (xmin, y)
        if xmax != xmin:
            yield (xmax, y)


def solve(data: str) -> tuple[int, int]:
    coords: list[Point] = [
        (x, y)
        for line in data.splitlines()
        for x, y in [tuple(map(int, line.split(",")))]
    ]

    compressed, decompress = compress_2d(coords)

    valid = build_valid(compressed)

    boxes: list[Box] = sorted(
        combinations(compressed, 2), key=lambda b: size(cast(Box, tuple(decompress(b))))
    )

    part1 = size(cast(Box, tuple(decompress(boxes[-1]))))
    part2 = 0
    for box in list(reversed(boxes)):
        if all(p in valid for p in rect_border_points(box)):
            part2 = size(cast(Box, tuple(decompress(box))))
            break

    return part1, part2
