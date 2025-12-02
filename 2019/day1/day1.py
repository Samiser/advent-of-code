def calculate_fuel_1(mass):
    return int(mass / 3) - 2

def calculate_fuel_2(mass):
    mass = int(mass / 3) - 2
    return 0 if mass < 1 else mass + calculate_fuel_2(mass)

if __name__ == "__main__":
    total = [0, 0]
    input_data = open("day1.txt", 'r')

    for mass in input_data.read().split('\n'):
        if mass:
            total[0] += calculate_fuel_1(int(mass))
            total[1] += calculate_fuel_2(int(mass))

    print("Part 1: {}".format(total[0]))
    print("Part 2: {}".format(total[1]))
