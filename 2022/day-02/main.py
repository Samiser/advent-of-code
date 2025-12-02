first = 0
second = 0

with open("input.txt") as f:
    for line in f.readlines():
        left = ord(line[:1]) - 64
        right = ord(line[2:3]) - 87

        first += 3 * ((-left + right - 2) % 3) + right
        second += (left + right) % 3 + 3 * right - 2

print(first)
print(second)
