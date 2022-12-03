from pprint import pprint


def read_data(filename="input.txt"):
    data = []
    with open(filename) as file:
        for line in file.readlines():
            rucksack = line.strip()

            data.append((set(rucksack[:len(rucksack)//2]),
                         set(rucksack[len(rucksack)//2:]),
                         ))
    return data


def priority_translator(char):
    if char.isupper():
        return ord(char) - 65 + 27
    else:
        return ord(char) - 96


def solve_1(data):
    # 10:21 to 10:34

    common_items = list()
    for first, second in data:
        common_item = first & second
        common_items.append(common_item)

    return sum([priority_translator(list(common_item)[0]) for common_item in common_items])


def solve_2(data):
    # 11:50 to 11:57
    common_items = list()

    for first, second, third in zip(data[::3], data[1::3], data[2::3]):
        common_item = set(first[0] | first[1]) & set(
            second[0] | second[1]) & set(third[0] | third[1])
        common_items.append(common_item)

    return sum([priority_translator(list(common_item)[0]) for common_item in common_items])


if __name__ == "__main__":
    data = read_data()
    result = solve_1(data)
    pprint(result)
    result = solve_2(data)
    pprint(result)
