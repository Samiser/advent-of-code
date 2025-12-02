grid = [[int(tree) for tree in row] for row in open("input.txt").read().splitlines()]
visible = [[0 for x in range(len(grid))] for y in range(len(grid[0]))] 
scores = [[1 for x in range(len(grid))] for y in range(len(grid[0]))] 
rotate = lambda g : list(map(list, zip(*reversed(g))))

for _ in range(4):
    for x, row in enumerate(grid):
        highest = -1
        for y, tree in enumerate(row):
            score = 0
            for t in row[y+1:]:
                score += 1
                if t >= tree: break
            scores[x][y] *= score
            if tree > highest:
                highest = tree
                visible[x][y] = 1
    grid, visible, scores = map(rotate, (grid, visible, scores))

print(sum(row.count(1) for row in visible))
print(max(map(max, scores)))
