from pprint import pprint
from dataclasses import dataclass


@dataclass
class Square():
    height: str
    upper: "Square"
    lower: "Square"
    left: "Square"
    right: "Square"
    steps_to_reach: int = 0


def read_data(filename="input.txt"):
    square_start = None
    square_top_left = None
    square_prev = None
    data = []
    with open(filename) as file:
        for line in file.readlines():
            data.append(list(line.strip()))
    return data


def find_start_end_position(data):
    START = "S"
    END = "E"
    start_position = end_position = (0, 0)
    for row_index, row in enumerate(data):
        if START in row:
            start_position = (row_index, row.index(START))
        if END in row:
            end_position = (row_index, row.index(END))
    return start_position, end_position


def solve_1(data):
    # 18:45 to 20:27
    MAX_ROWS = len(data)
    MAX_COLUMNS = len(data[0])
    start_position, end_position = find_start_end_position(data)
    walk_grid = [[0 for _ in range(MAX_COLUMNS)]
                 for _ in range(MAX_ROWS)]
    current_height = 0
    walk_grid[0][0] = current_height
    reachable_heights = set()
    investigating_heights = set()
    visited_heights = set()
    reachable_heights.add(start_position)
    for i in range(100000):
        visited_heights |= investigating_heights
        investigating_heights = reachable_heights
        reachable_heights = set()

        for position in investigating_heights:
            current_height = ord(data[position[0]][position[1]])
            if current_height == ord("S"):
                current_height = ord("a")
            if end_position == position:
                return i
            for row, column in [(position[0]+row, position[1]+column) for row, column in [(1, 0), (0, 1), (-1, 0), (0, -1)]]:
                if 0 <= row < MAX_ROWS and 0 <= column < MAX_COLUMNS:
                    height_other = ord(
                        data[row][column]) if data[row][column] != "E" else ord("z")
                    if (height_other - current_height) <= 1:
                        if (row, column) not in visited_heights:
                            reachable_heights.add((row, column))
                            walk_grid[row][column] = i
    return i


def find_all_a(data):
    a = list()
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char == "a":
                a.append((i, j))
    return a


def solve_2(data):
    # 20:28 to 20:36
    MAX_ROWS = len(data)
    MAX_COLUMNS = len(data[0])
    start_position, end_position = find_start_end_position(data)
    walk_grid = [[0 for _ in range(MAX_COLUMNS)]
                 for _ in range(MAX_ROWS)]
    current_height = 0
    walk_grid[0][0] = current_height
    reachable_heights = set(find_all_a(data))
    investigating_heights = set()
    visited_heights = set()
    reachable_heights.add(start_position)
    for i in range(100000):
        visited_heights |= investigating_heights
        investigating_heights = reachable_heights
        reachable_heights = set()

        for position in investigating_heights:
            current_height = ord(data[position[0]][position[1]])
            if current_height == ord("S"):
                current_height = ord("a")
            if end_position == position:
                return i
            for row, column in [(position[0]+row, position[1]+column) for row, column in [(1, 0), (0, 1), (-1, 0), (0, -1)]]:
                if 0 <= row < MAX_ROWS and 0 <= column < MAX_COLUMNS:
                    height_other = ord(
                        data[row][column]) if data[row][column] != "E" else ord("z")
                    if (height_other - current_height) <= 1:
                        if (row, column) not in visited_heights:
                            reachable_heights.add((row, column))
                            walk_grid[row][column] = i
    return i


if __name__ == "__main__":
    pprint(read_data("input_test.txt"))

    print("Test part 1: ", solve_1(read_data("input_test.txt")))
    print("Test part 2: ", solve_2(read_data("input_test.txt")))

    print("Real part 1: ", solve_1(read_data("input.txt")))
    print("Real part 2: ", solve_2(read_data("input.txt")))
