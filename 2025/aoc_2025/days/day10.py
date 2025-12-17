from dataclasses import dataclass
from itertools import combinations
from math import gcd


@dataclass
class Line:
    lights: list[bool]
    buttons: list[tuple[int, ...]]
    joltage: list[int]

    def __init__(self, s: str) -> None:
        parts = s.split(" ")
        self.lights = [c == "#" for c in parts[0][1:-1]]
        self.buttons = [tuple(int(i) for i in x[1:-1].split(",")) for x in parts[1:-1]]
        self.joltage = [int(i) for i in parts[-1][1:-1].split(",")]


def toggle(lights: list[bool], instructions: tuple[int, ...]) -> list[bool]:
    for i in instructions:
        lights[i] = not lights[i]

    return lights


def solve_lights(l: Line) -> int:
    lights = [False] * len(l.lights)
    for i in range(10):
        for combo in combinations(l.buttons, i):
            for button in combo:
                lights = toggle(lights, button)
            if lights == l.lights:
                return i
            lights = [False] * len(l.lights)

    raise Exception(f"Failed to solve lights for {l}")


def build_system(line: Line) -> tuple[list[list[int]], list[int], list[int]]:
    b = line.joltage
    A: list[list[int]] = [[] for _ in b]
    c: list[int] = []
    for btn in line.buttons:
        c.append(min(b[j] for j in btn))
        for i in range(len(b)):
            A[i].append(1 if i in btn else 0)
    return A, b, c


def swaprow(A: list[list[int]], b: list[int], i: int, j: int) -> None:
    if i != j:
        A[i], A[j] = A[j], A[i]
        b[i], b[j] = b[j], b[i]


def swapcol(A: list[list[int]], c: list[int], i: int, j: int) -> None:
    if i != j:
        for k in range(len(A)):
            A[k][i], A[k][j] = A[k][j], A[k][i]
        c[i], c[j] = c[j], c[i]


def reducerow(A: list[list[int]], b: list[int], i: int, j: int) -> None:
    if A[i][i] != 0:
        x = A[i][i]
        y = -A[j][i]
        d = gcd(x, y)
        A[j] = [(y * A[i][k] + x * A[j][k]) // d for k in range(len(A[i]))]
        b[j] = (y * b[i] + x * b[j]) // d


def reduce(
    A: list[list[int]], b: list[int], c: list[int]
) -> tuple[list[list[int]], list[int], list[int]]:
    for i in range(len(A[0])):
        I: list[int] = []
        k = i
        while len(I) == 0 and k < len(A[0]):
            swapcol(A, c, i, k)
            I = [j for j in range(i, len(A)) if A[j][i] != 0]
            k += 1
        if len(I) == 0:
            break
        swaprow(A, b, i, I[0])
        for j in range(i + 1, len(A)):
            reducerow(A, b, i, j)

    I = [i for i in range(len(A)) if any(a != 0 for a in A[i])]
    A = [A[i] for i in I]
    b = [b[i] for i in I]

    for i in range(len(A) - 1, -1, -1):
        for j in range(i):
            reducerow(A, b, i, j)

    return A, b, c


def paramcomb(nparam: int, c: list[int]) -> list[list[int]]:
    if nparam == 0:
        return [[]]
    ret: list[list[int]] = []
    for i in range(c[-nparam] + 1):
        ret += [[i, *l] for l in paramcomb(nparam - 1, c)]
    return ret


def solve_system_min_sum(A: list[list[int]], b: list[int], c: list[int]) -> int:
    k = len(A[0]) - len(A)
    mins = 10**10
    for params in paramcomb(k, c):
        sol = sum(params)
        for i in range(len(A)):
            cc = (params[j] * A[i][len(A[0]) - k + j] for j in range(len(params)))
            s = b[i] - sum(cc)
            a = s // A[i][i]
            if a < 0 or s % A[i][i] != 0:
                sol = 10**10
                break
            sol += a
        if sol < mins:
            mins = sol
    return mins


def solve_machine(line: Line) -> int:
    A, b, c = build_system(line)
    A2, b2, c2 = reduce(A, b, c)
    return solve_system_min_sum(A2, b2, c2)


def solve(data: str) -> tuple[int, int]:
    part1 = 0
    part2 = 0

    for line in data.splitlines():
        part1 += solve_lights(Line(line))
        part2 += solve_machine(Line(line))

    return part1, part2
