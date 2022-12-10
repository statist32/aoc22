from pprint import pprint
from collections import defaultdict


def read_data(filename="input.txt"):
    data = []
    with open(filename) as file:
        for line in file.readlines():
            line = line.strip()
            if " " in line:
                instruction, value = line.split(" ")
                data.append((instruction, int(value)))
            else:
                data.append((line, 0))

    return data


def calc_cycles(data):
    cycles = [1]
    for instruction, value in data:
        cycles.append(cycles[-1])
        if instruction == "addx":
            cycles.append(cycles[-1])
            cycles[-1] += value
    return cycles


def solve_1(data):
    # 9:31 to 10:22
    # noop before add in one cycle
    cycles = calc_cycles(data)

    return sum([i * cycles[i-1] for i in range(20, len(cycles)-1, 40)])


def solve_2(data):
    # 10:23 to 10:51
    SPRITE = "###"
    CRT_HEIGHT = 6
    CRT_WIDTH = 40
    crt = []
    cycles = calc_cycles(data)
    for row in range(CRT_HEIGHT):
        crt_row = ""
        for pixel in range(0, CRT_WIDTH):
            sprite_position = set(
                range(cycles[pixel+row*CRT_WIDTH]-1, cycles[pixel+row*CRT_WIDTH]+2))
            if pixel in sprite_position:
                crt_row += "#"
            else:
                crt_row += "."
        crt.append(crt_row)
    pprint(crt)


if __name__ == "__main__":
    data = read_data("input_test.txt")
    # pprint(data)
    # print("Test part 1: ", solve_1(data))
    print("Test part 2: ", solve_2(data))

    data = read_data("input.txt")
    # print("Real part 1: ", solve_1(data))
    print("Real part 2: ", solve_2(data))
