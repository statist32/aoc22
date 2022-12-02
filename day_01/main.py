from pprint import pprint


def read_data(filename="input.txt"):
    data = []
    elf = []
    with open(filename) as file:
        for line in file.readlines():
            if line != "\n":
                elf.append(int(line.strip()))
            else:
                data.append(elf)
                elf = []
    return data


def calculate_max_calories_one(elves_calories):
    total_calories = [sum(elf_calories) for elf_calories in elves_calories]
    max_calories = max(total_calories)
    return max_calories


def calculate_max_calories_three(elves_calories):
    total_calories = [sum(elf_calories) for elf_calories in elves_calories]
    max_calories = sum(sorted(total_calories)[-3:])
    return max_calories


if __name__ == "__main__":
    data = read_data()
    max_calories = calculate_max_calories_one(data)
    max_calories = calculate_max_calories_three(data)
    print(max_calories)
