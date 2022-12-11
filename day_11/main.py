from pprint import pprint
from dataclasses import dataclass, field
from math import floor


@dataclass
class Monkey():
    id: int
    operation: tuple[str, int]
    test: tuple[int, tuple[int, int]]
    items:  list[int] = field(default_factory=list)
    inspection_count: int = 0

    def throw_item_to(self, item, monkeys):
        goal_monkey = self.test["false"]
        if not item % self.test["number"]:
            goal_monkey = self.test["true"]
        DIVISOR = 9699690

        monkeys[goal_monkey].catch_item(item % DIVISOR)
        # print(item, self.id, goal_monkey)

    def catch_item(self, item):
        self.items.append(item)

    def inspect_items(self, monkeys):
        self.items = [self.inspect_item(item) for item in self.items]
        self.inspection_count += len(self.items)
        while len(self.items):
            item = self.items.pop()
            self.throw_item_to(item, monkeys)

    def inspect_item(self, item):
        operator, value = self.operation
        worry_level = item
        if "+" in operator:
            worry_level += int(value) if not "old" in value else worry_level
        elif "*" in operator:
            worry_level *= int(value) if not "old" in value else worry_level
        worry_level = floor(worry_level/1)
        # print(self.operation, self.id, item, worry_level)
        return worry_level


def read_data(filename="input.txt"):
    data = []
    monkey_id = 0
    starting_items = []
    operation = tuple()
    test = {}
    with open(filename) as file:
        for line in file.readlines():
            line = line.strip()
            if line.startswith("Monkey"):
                data.append(Monkey(monkey_id, operation, test, starting_items))
                monkey_id = int(line.split(" ")[1][:-1])
            elif "Starting items:" in line:
                starting_items = [int(item.replace(",", ""))
                                  for item in line.split()[2:]]
            elif "Operation:" in line:
                operation = (line.split(" ")[-2:])
            elif "Test:" in line:
                test = {}
                test["number"] = int(line.split(" ")[-1])
            elif "If true:" in line:
                test["true"] = int(line.split(" ")[-1])
            elif "If false:" in line:
                test["false"] = int(line.split(" ")[-1])
    data.append(Monkey(monkey_id, operation, test, starting_items))

    return data[1:]


def solve_1(data):
    # 16:48 to 18:00
    for i in range(20):
        for monkey in data:
            monkey.inspect_items(data)
    pprint(data)
    a, b = sorted([monkey.inspection_count for monkey in data])[-2:]
    return a*b


def solve_2(data):
    # 18:04 to 18:12
    divisor = 1
    for number in [monkey.test["number"] for monkey in data]:
        divisor *= number
    print(divisor)
    for i in range(10000):
        for monkey in data:
            monkey.inspect_items(data)
    # pprint(data)
    a, b = sorted([monkey.inspection_count for monkey in data])[-2:]
    return a*b


if __name__ == "__main__":
    data = read_data("input_test.txt")
    # pprint(data)
    # print("Test part 1: ", solve_1(data))
    print("Test part 2: ", solve_2(data))

    data = read_data("input.txt")
    # print("Real part 1: ", solve_1(data))
    print("Real part 2: ", solve_2(data))
