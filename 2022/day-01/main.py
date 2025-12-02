with open("input.txt") as f:
    elves = sorted(sum(map(int, elf.splitlines())) for elf in f.read().split('\n\n'))

print(elves[-1])
print(sum(elves[-3:]))
