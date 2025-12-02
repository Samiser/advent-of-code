from collections import Counter

def valid(start, end):
    for number in range(start, end):
        prev = []
        double = False
        ordered = True

        for n in str(number):
            if len(prev) > 0:
                if n < prev[-1]:
                    ordered = False
                elif prev.count(n) > 0:
                    double = True

            prev.append(n)

        if ordered: 
            yield double, 2 in Counter(prev).values()

if __name__ == "__main__":
    total1 = 0
    total2 = 0

    for rule1, rule2 in valid(153517, 630395):
       if rule1:
            total1 += 1 
       if rule1 and rule2:
            total2 += 1 
         
    print("Part 1:", total1)
    print("Part 2:", total2)
