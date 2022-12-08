from pprint import pprint


def read_data(filename="input.txt"):
    data = []
    with open(filename) as file:
        for line in file.readlines():
            data.append([int(entry) for entry in list(line.strip())])
    return data


def is_viewable_column(data, row, column):
    tree_height = data[row][column]
    trees_column = [row[column] for row in data]
    trees_above = trees_column[:row]
    trees_below = trees_column[row+1:]
    is_viewable = max(trees_above) < tree_height or max(
        trees_below) < tree_height
    return is_viewable


def is_viewable_row(data, row, column):
    tree_height = data[row][column]
    trees_row = data[row]
    trees_left = trees_row[:column]
    trees_right = trees_row[column+1:]
    is_viewable = max(trees_left) < tree_height \
        or max(trees_right) < tree_height
    return is_viewable


def is_viewable(data, row, column):
    return is_viewable_column(data, row, column) or is_viewable_row(data, row, column)


def solve_1(data):
    # 13:33 to 14:08
    sum = 2*(len(data)+len(data[0]))-4
    data_inner = [row[1:-1] for row in data][1:-1]
    for row_index, row in enumerate(data_inner):
        for column_index, _ in enumerate(row):
            viewable = is_viewable(data, row_index+1, column_index+1)
            sum += int(viewable)
    return sum


def calc_score_direction(trees, tree_height):
    score = 0
    for tree in trees:
        if tree < tree_height:
            score += 1
        else:
            score += 1
            break
    return score


def calc_score(data, row, column):
    tree_height = data[row][column]
    trees_row = data[row]
    amount_trees_left = calc_score_direction(
        list(reversed(trees_row[:column])), tree_height)
    amount_trees_right = calc_score_direction(
        trees_row[column+1:], tree_height)

    trees_column = [row[column] for row in data]
    amount_trees_upper = calc_score_direction(
        list(reversed(trees_column[:row])), tree_height)
    amount_trees_lower = calc_score_direction(
        trees_column[row+1:], tree_height)

    return amount_trees_left * amount_trees_right * amount_trees_upper * amount_trees_lower


def solve_2(data):
    # 14:08 to 14:54
    max_score = 0
    for row_index, row in enumerate(data):
        for column_index, column in enumerate(row):
            score = calc_score(data, row_index, column_index)
            max_score = max(score, max_score)
    return max_score


if __name__ == "__main__":
    data = read_data("input_test.txt")
    pprint(data)
    print("Test part 1: ", solve_1(data))
    print("Test part 2: ", solve_2(data))

    data = read_data("input.txt")
    print("Real part 1: ", solve_1(data))
    print("Real part 2: ", solve_2(data))
