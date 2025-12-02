from math import prod,lcm

class Monkey:
    def __init__(self, lines):
        _name, items, operation, test, true_target, false_target = lines.splitlines()
        self.items = list(map(int, items[18:].split(", ")))
        self.operation = eval(f"lambda old : {operation[19:]}")
        self.test = int(test[21:])
        self.true_target = int(true_target[29:])
        self.false_target = int(false_target[30:])
        self.inspected = 0

    def inspect_items(self, mod=None):
        self.inspected += len(self.items)
        if mod == None:
            self.items = [self.operation(item) // 3 for item in self.items]       
        else:
            self.items = [self.operation(item) % mod for item in self.items]       

    def throw_items(self, monkeys):
        for item in self.items:
            if item % self.test == 0:
                monkeys[self.true_target].catch(item)
            else:
                monkeys[self.false_target].catch(item)
        self.items = []

    def catch(self, item):
        self.items.append(item)

def solve(text, part):
    monkeys = [Monkey(m) for m in text.split('\n\n')]
    mod = prod([monkey.test for monkey in monkeys])

    for r in range(20) if part == "part 1" else range(10000):
        for monkey in monkeys:
            match part:
                case "part 1": monkey.inspect_items()
                case "part 2": monkey.inspect_items(mod)
            monkey.throw_items(monkeys)

    return prod(sorted([m.inspected for m in monkeys])[-2:])

if __name__ == '__main__':
    text = open("input.txt").read()

    print(solve(text, "part 1"))
    print(solve(text, "part 2"))
