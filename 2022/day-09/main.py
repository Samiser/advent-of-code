dirs = {'U': (0, +1), 'D': (0, -1), 'L': (-1, 0), 'R': (+1, 0)}
rope = [(0, 0)] * 10
seen = [set([knot]) for knot in rope]
move = lambda pos,d : (pos[0]+d[0], pos[1]+d[1])

for m in open("input.txt").read().splitlines():
    for _ in range(int(m[2:])):
        rope[0] = move(rope[0], dirs[m[0]])
        for part in range(1, len(rope)):
            dist = [rope[part-1][x] - rope[part][x] for x in (0,1)]
            if abs(max(dist, key=abs)) > 1:
                rope[part] = move(rope[part], [x//(abs(x) or 1) for x in dist])
                seen[part].add(rope[part])

print(len(seen[1]), len(seen[-1]))
