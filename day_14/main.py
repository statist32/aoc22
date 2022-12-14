from pprint import pprint


def read_data(filename="input.txt"):
    data = set()
    with open(filename) as file:
        for line in file.readlines():
            line = line.strip()
            rocks = [[int(x) for x in rock.split(",")]
                     for rock in line.split(" -> ")]
            for start, end in zip(rocks, rocks[1:]):
                if start[0] == end[0]:
                    sequence = list(range(min(start[1], end[1]),
                                          max(start[1], end[1])+1))

                    data |= set([(start[0], seq) for seq in sequence])
                else:
                    sequence = list(range(min(start[0], end[0]),
                                          max(start[0], end[0])+1))
                    data |= set([(seq, start[1]) for seq in sequence])
    MIN_COLUMNS = min([rock[0] for rock in rocks])
    return data


def print_reservoir(rocks, sand):
    ROCK = "#"
    SAND = "°"
    MAX_ROWS = max([rock[1] for rock in rocks])
    MIN_COLUMNS = min([rock[0] for rock in rocks])
    MAX_COLUMNS = max([rock[0] for rock in rocks])
    reservoir = [["." for _ in range(MIN_COLUMNS, MAX_COLUMNS+1)]
                 for _ in range(MAX_ROWS+1)]

    for rock in list(rocks):
        reservoir[rock[1]][rock[0]] = ROCK
    for sand in list(sand):
        reservoir[sand[1]][sand[0]] = SAND

    for row in reservoir:
        print("".join(row))
    print("\n"*3)


def sand_fall_trajectory_1(starting_position, rocks, sand):
    MAX_COLUMNS = max([rock[0] for rock in rocks])
    MAX_ROWS = max([rock[1] for rock in rocks])
    obstacles = rocks
    obstacles |= sand
    position = starting_position
    for _ in range(MAX_ROWS+1):
        if not (0 <= position[0] <= MAX_COLUMNS and 0 <= position[1] <= MAX_ROWS):
            print("Out of range", position)
            return False
        elif (position[0], position[1]+1) not in obstacles:
            # down
            position = (position[0], position[1]+1)
        elif (position[0], position[1]+1) in obstacles and (position[0]-1, position[1]+1) not in obstacles:
            # left
            position = (position[0]-1, position[1]+1)
        elif (position[0], position[1]+1) in obstacles and (position[0]+1, position[1]+1) not in obstacles:
            # right
            position = (position[0]+1, position[1]+1)
        else:
            sand.add(position)
    return True


def solve_1(data):
    # 9:39 to 10:38
    MIN_COLUMNS = min([rock[0] for rock in data])
    rocks = set([(rock[0]-MIN_COLUMNS, rock[1]) for rock in data])

    SAND_SOURCE = (500 - MIN_COLUMNS, 0)
    sand = set()

    old_len = -1
    while old_len < len(sand):
        old_len = len(sand)
        sand_fall_trajectory_1(SAND_SOURCE, rocks, sand)

    print_reservoir(rocks, sand)
    return len(sand)


def sand_fall_trajectory_2(starting_position, rocks, sand):
    MAX_ROWS = max([rock[1] for rock in rocks])
    obstacles = rocks
    obstacles |= sand
    position = starting_position
    for _ in range(MAX_ROWS+2):
        if position in obstacles:
            sand.add(position)
            return False
        elif (position[0], position[1]+1) not in obstacles:
            # down
            position = (position[0], position[1]+1)
        elif (position[0], position[1]+1) in obstacles and (position[0]-1, position[1]+1) not in obstacles:
            # left
            position = (position[0]-1, position[1]+1)
        elif (position[0], position[1]+1) in obstacles and (position[0]+1, position[1]+1) not in obstacles:
            # right
            position = (position[0]+1, position[1]+1)
        else:
            sand.add(position)
    return True


def solve_2(data):
    # 10:47 to 12:05
    MAX_ROWS = max([rock[1] for rock in data])
    MIN_COLUMNS = min([rock[0] for rock in data])
    BEDROCK_RANGE = 500
    data |= set([(i, MAX_ROWS+2)
                 for i in range(-BEDROCK_RANGE+MIN_COLUMNS, BEDROCK_RANGE+MIN_COLUMNS)])
    rocks = set([(rock[0]-MIN_COLUMNS+BEDROCK_RANGE, rock[1])
                for rock in data])
    SAND_SOURCE = (500 - MIN_COLUMNS+BEDROCK_RANGE, 0)

    sand = set()
    old_len = -1
    while old_len < len(sand):
        old_len = len(sand)
        if not old_len % 1000:
            print(old_len)
        sand_fall_trajectory_2(SAND_SOURCE, rocks, sand)

    # print_reservoir(rocks, sand)
    return len(sand)


if __name__ == "__main__":
    pprint(read_data("input_test.txt"))

    print("Test part 1: ", solve_1(read_data("input_test.txt")))
    print("Test part 2: ", solve_2(read_data("input_test.txt")))

    print("Real part 1: ", solve_1(read_data("input.txt")))
    print("Real part 2: ", solve_2(read_data("input.txt")))
