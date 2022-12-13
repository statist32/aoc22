from pprint import pprint
from itertools import zip_longest


def read_data(filename="input.txt"):
    data = []
    with open(filename) as file:
        left = None
        right = None
        for line in file.readlines():
            line = line.strip()
            if line == "":
                data.append((left, right))
                left = None
                right = None
            else:
                if left is None:
                    left = eval(line)
                else:
                    right = eval(line)
        data.append((left, right))
    return data


def compare_lists(packet_left, packet_right):
    for left, right in zip_longest(packet_left, packet_right):
        if type(left) == type(right) == int:
            if left < right:
                return True
            elif left > right:
                return False
        elif type(left) == type(right) == list:
            comparison = compare_lists(left, right)
            if comparison == False:
                return False
            elif comparison == True:
                return True
        elif left is not None and right is None:
            return False
        elif left is None and right is not None:
            return True
        elif type(left) == int and type(right) == list:
            comparison = compare_lists([left], right)
            if comparison == False:
                return False
            elif comparison == True:
                return True
        elif type(left) == list and type(right) == int:
            comparison = compare_lists(left, [right])
            if comparison == False:
                return False
            elif comparison == True:
                return True


def solve_1(data):
    # 9:50 to 10:41
    comparisons = list()
    for left, right in data:
        comparisons.append(compare_lists(left, right))
    return sum([i+1 for i, comparison in enumerate(comparisons) if comparison])


def solve_2(data):
    # 10:41 to 10:54
    DIVIDER_PACKET_1 = [[2]]
    DIVIDER_PACKET_2 = [[6]]

    packets = [DIVIDER_PACKET_1, DIVIDER_PACKET_2]
    for left, right in data:
        packets.append(left)
        packets.append(right)
    for _ in range(len(packets)-1):
        for j in range(len(packets)-1):
            comparison = compare_lists(packets[j], packets[j+1])
            if comparison == False:
                packets[j], packets[j+1] = packets[j+1], packets[j]
    return (packets.index(DIVIDER_PACKET_1)+1) * (packets.index(DIVIDER_PACKET_2)+1)


if __name__ == "__main__":
    pprint(read_data("input_test.txt"))

    print("Test part 1: ", solve_1(read_data("input_test.txt")))
    print("Test part 2: ", solve_2(read_data("input_test.txt")))

    print("Real part 1: ", solve_1(read_data("input.txt")))
    print("Real part 2: ", solve_2(read_data("input.txt")))
