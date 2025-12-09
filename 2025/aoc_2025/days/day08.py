from math import prod, dist
from sys import modules


class DSU:
    def __init__(self, n: int) -> None:
        self.parent: list[int] = list(range(n))
        self.rank: list[int] = [0] * n
        self.size: list[int] = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> None:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return

        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]

        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1


def solve(data: str) -> tuple[int, int]:
    limit = 10 if "pytest" in modules else 1000

    coords: list[tuple[int, int, int]] = [
        (x, y, z)
        for line in data.splitlines()
        for x, y, z in [tuple(map(int, line.split(",")))]
    ]
    n = len(coords)

    edges = [
        (dist(coords[i], coords[j]), i, j) for i in range(n) for j in range(i + 1, n)
    ]
    edges.sort(key=lambda e: e[0])

    dsu = DSU(n)

    last_two: tuple[int, int] = 0, 0
    largest_three: list[int] = []

    for k in range(len(edges)):
        _, i, j = edges[k]
        dsu.union(i, j)
        roots = {dsu.find(i) for i in range(n)}

        if k == limit:  # part 1
            sizes = [dsu.size[root] for root in roots]
            sizes.sort()
            largest_three = sizes[-3:]

        if len(roots) == 1:  # part 2
            last_two = coords[i][0], coords[j][0]
            break

    return prod(largest_three), prod(last_two)
