from pprint import pprint
from collections import deque


def read_data(filename="input.txt"):
    instructions = []
    stacks = []
    stacks_temp = []
    with open(filename) as file:
        for line in file.readlines():
            if line.startswith("move"):
                amount, start, end = (line.strip().removeprefix("move ").replace(
                    " from ", ",").replace(" to ", ",").split(","))
                instructions.append((int(amount), int(start), int(end)))
            else:
                if line != "\n":
                    stacks_temp.append(line.replace("\n", ""))
        stack_amount = 0
        for line in reversed(stacks_temp):
            if line.startswith(" 1"):
                stack_amount = int(line[-2])
                stacks.extend([deque() for i in range(stack_amount)])
            else:
                for i in range(0, stack_amount):
                    entry = line[i*4+1].strip()
                    if entry:
                        stacks[i].append(entry)
    return (stacks, instructions)


def solve_1(stacks, instructions):
    # 9:12 to 9:39
    for amount, start, end in instructions:
        for amount in range(amount):
            crate = stacks[start-1].pop()
            stacks[end-1].append(crate)
    return "".join([stack[-1] for stack in stacks])


def solve_2(stacks, instructions):
    # 9:40 to 9:50
    for amount, start, end in instructions:
        crates = []
        for amount in range(amount):
            crates.append(stacks[start-1].pop())
        crates.reverse()
        stacks[end-1].extend(crates)
        pprint(stacks)
    return "".join([stack[-1] for stack in stacks])


if __name__ == "__main__":
    data = read_data("input_test.txt")
    pprint(data)
    print("Test part 1: ", solve_1(*read_data("input_test.txt")))
    print("Test part 2: ", solve_2(*read_data("input_test.txt")))

    print("Real part 1: ", solve_1(*read_data("input.txt")))
    print("Real part 2: ", solve_2(*read_data("input.txt")))
