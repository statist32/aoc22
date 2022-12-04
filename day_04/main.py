from pprint import pprint


def read_data(filename="input.txt"):
    data = []
    with open(filename) as file:
        for line in file.readlines():
            pair_1, pair_2 = line.strip().split(",")
            pair_1_start, pair_1_end = pair_1.split("-")
            pair_2_start, pair_2_end = pair_2.split("-")
            set_1 = set(range(int(pair_1_start), int(pair_1_end)+1))
            set_2 = set(range(int(pair_2_start), int(pair_2_end)+1))
            data.append((set_1, set_2))

    return data


def solve_1(pairs):
    # 11:35 to 11:44
    return sum([pair_1.issuperset(pair_2) or pair_1.issubset(pair_2) for pair_1, pair_2 in pairs])


def solve_2(pairs):
    # 11:44 to 11:46
    return sum([bool(pair_1 & pair_2) for pair_1, pair_2 in pairs])


if __name__ == "__main__":
    data = read_data()
    result = solve_1(data)
    pprint(result)
    result = solve_2(data)
    pprint(result)
