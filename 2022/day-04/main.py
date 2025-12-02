with open("input.txt") as f:
    pairs = map(lambda l : list(map(lambda p : list(map(int, p.split('-'))), l.split(','))), f.read().splitlines())
    sets = list(map(lambda p : list(map(lambda x : set(range(x[0], x[1] + 1)), p)), pairs))

    print(sum(map(lambda p : p[0].issubset(p[1]) or p[1].issubset(p[0]), sets)))
    print(sum(map(lambda p : bool(set.intersection(p[0], p[1])), sets)))
