def solve(data: str) -> tuple[int, int]:
    lines = data.splitlines()

    split_count = 0
    paths = [0] * len(lines[0])
    paths[lines[0].find("S")] = 1

    for line in lines:
        for pos, char in enumerate(line):
            if char == "^" and paths[pos] > 0:
                split_count += 1
                paths[pos - 1] += paths[pos]
                paths[pos + 1] += paths[pos]
                paths[pos] = 0

    return split_count, sum(paths)
