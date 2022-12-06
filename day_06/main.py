from pprint import pprint


def read_data(filename="input.txt"):
    data = []
    with open(filename) as file:
        for line in file.readlines():
            data = line
    return data


def solve_1(data):
    # 9:11 to 9:20
    AMOUNT = 4
    for index, sequence in enumerate(zip(data[:], data[1:], data[2:], data[3:])):
        if len(set(sequence)) == AMOUNT:
            return index+AMOUNT


def solve_2(data):
    # 9:21 to 9:23
    AMOUNT = 14
    for index, sequence in enumerate(zip(*[data[i:] for i in range(AMOUNT)])):
        if len(set(sequence)) == AMOUNT:
            return index+AMOUNT


if __name__ == "__main__":
    data = read_data("input_test.txt")
    pprint(data)
    print("Test part 1: ", solve_1(data))
    print("Test part 2: ", solve_2(data))

    data = read_data("input.txt")
    print("Real part 1: ", solve_1(data))
    print("Real part 2: ", solve_2(data))
