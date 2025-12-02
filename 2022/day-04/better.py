import re

with open("input.txt") as f:
    pairs = list(map(lambda l : list(map(int, re.findall('\d+', l))), f.read().splitlines()))
    print(sum(map(lambda p : p[0] <= p[2] and p[1] >= p[3] or p[2] <= p[0] and p[3] >= p[1], pairs)))
    print(sum(map(lambda p : p[0] <= p[3] and p[2] <= p[1], pairs)))
