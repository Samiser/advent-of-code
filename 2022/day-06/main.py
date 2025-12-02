t = open("input.txt").read()

for s in 4,14:
    print(next((x+s for x in range(len(t)) if len(t[x:x+s]) == len(set(t[x:x+s])))))
