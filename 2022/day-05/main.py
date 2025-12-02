raw_s, raw_i = open("input.txt").read().split("\n\n")

for rotation in (-1, 1):
    stacks = list(map(lambda s: "".join(s).strip(), zip(*raw_s.splitlines()[:-1])))[1::4]
    for i in list(map(lambda i : list(map(int, i.split(" ")[1::2])), raw_i.splitlines())):
        n, src, dst = i[0], stacks[i[1] - 1], stacks[i[2] - 1]
        stacks[i[1] - 1], stacks[i[2] - 1] = (src[n:], src[:n][::rotation] + dst)
    print("".join(map(lambda stack: stack[0], stacks)))
