import re
from itertools import accumulate

instructions = map(int, re.sub(r'[noop|addx]', '0', open('input.txt').read()).split())
part1, part2 = 0, ''

for cycle, X in enumerate(accumulate(instructions, initial=1), start=1):
    part1 += cycle * X if cycle % 40 == 20 else 0
    part2 += '# ' if abs((cycle-1)%40 - X) < 2 else '\n' if cycle % 40 == 0 else '  '

print(part1)
print(part2)
