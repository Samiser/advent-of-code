def run(code):
    for a, b, c, d in (code[i:i + 4] for i in range(0, len(code) - 3, 4)):
        if a == 99:
            break
        elif a == 1:
            code[d] = code[b] + code[c]
        elif a == 2:
            code[d] = code[b] * code[c]

    return code[0]


if __name__ == "__main__":
    input_data = open("day2.txt", 'r')
    code = [int(i) for i in input_data.read().split(',')]

    code[1] = 12
    code[2] = 2

    for noun in range(99):
        for verb in range(99):
            code[1] = noun
            code[2] = verb
            if run(code.copy()) == 19690720:
                print("Noun is ", noun)
                print("Verb is ", verb)
                break
