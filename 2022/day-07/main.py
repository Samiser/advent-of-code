from collections import defaultdict
from itertools import accumulate

tree = defaultdict(int)
location = []

for line in open('input.txt'):
    match line.split():
        case ['$', 'cd', '/']:
            location = ['/']
        case ['$', 'cd', '..']:
            location.pop()
        case ['$', 'cd', d]:
            location.append(d)
        case ['$', 'ls']:
            pass
        case ['dir', d]:
            pass
        case [size, file]:
            for path in accumulate(location): tree[path] += int(size)

print(sum(size for size in tree.values() if size <= 100000))
print(min(size for size in tree.values() if size >= tree['/'] - 40000000))
