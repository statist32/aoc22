from pprint import pprint
from math import hypot
from dataclasses import dataclass


@dataclass
class Position():
    x: int = 0
    y: int = 0

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return hypot(dx, dy)

    def touches(self, other):
        distance = self.distance(other)
        return distance < 2

    def move_towards(self, other):
        if other.x < self.x:
            # head left of tail
            self.x -= 1
        elif other.x > self.x:
            # head right of tail
            self.x += 1
        if other.y < self.y:
            # head left of tail
            self.y -= 1
        elif other.y > self.y:
            # head right of tail
            self.y += 1

    def move(self, direction):
        if direction == "U":
            self.y += 1
        elif direction == "D":
            self.y -= 1
        elif direction == "L":
            self.x -= 1
        elif direction == "R":
            self.x += 1


def read_data(filename="input.txt"):
    data = []
    with open(filename) as file:
        for line in file.readlines():
            direction, amount = line.strip().split(" ")
            data.append((direction, int(amount)))

    return data


def solve_1(data):
    # 8:36 to 9:13
    head_position = Position(0, 0)
    tail_position = Position(0, 0)
    visited_positions = set((0, 0))
    for direction, amount in data:
        for _ in range(amount):
            head_position.move(direction)
            if not tail_position.touches(head_position):
                tail_position.move_towards(head_position)
                visited_positions.add((tail_position.x, tail_position.y))
    return len(visited_positions)


def solve_2(data):
    # 9:13 to 9:31
    KNOTS = 10
    positions = [Position(0, 0) for _ in range(KNOTS)]
    visited_positions = set()
    for direction, amount in data:
        for _ in range(amount):
            for index, position in enumerate(zip(positions[0:], positions[1:])):
                position_previous, position_current = position
                if index == 0:
                    position_previous.move(direction)

                if not position_current.touches(position_previous):
                    position_current.move_towards(position_previous)
                if index == KNOTS - 2:
                    visited_positions.add(
                        (position_current.x, position_current.y))

    return len(visited_positions)


if __name__ == "__main__":
    data = read_data("input_test.txt")
    pprint(data)
    print("Test part 1: ", solve_1(data))
    print("Test part 2: ", solve_2(data))

    data = read_data("input.txt")
    print("Real part 1: ", solve_1(data))
    print("Real part 2: ", solve_2(data))
