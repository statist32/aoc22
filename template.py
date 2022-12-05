from pprint import pprint


def read_data(filename="input.txt"):
    data = []
    with open(filename) as file:
        for line in file.readlines():
            pass

    return data


def solve_1(data):
    #
    pass


def solve_2(data):
    #
    pass


if __name__ == "__main__":
    data = read_data("input_test.txt")
    pprint(data)
    print("Test part 1: ", solve_1(data))
    print("Test part 2: ", solve_2(data))

    data = read_data("input.txt")
    print("Real part 1: ", solve_1(data))
    print("Real part 2: ", solve_2(data))
