from pprint import pprint
from dataclasses import dataclass, field


@dataclass
class File():
    _name: str
    _size: int

    @property
    def name(self):
        return self._name

    @property
    def size(self):
        return self._size


@dataclass
class Directory():
    _name: str
    parent: "Directory"
    directories:  list["Directory"] = field(default_factory=list)
    files: list[File] = field(default_factory=list)

    @property
    def name(self):
        return self._name

    @property
    def size(self):
        return sum([dir.size for dir in self.directories]) + sum([file.size for file in self.files])

    @property
    def size_lower(self):
        MAX = 100000
        total = 0
        for dir in self.directories:
            size = dir.size
            if size <= MAX:
                total += size
            total += dir.size_lower
        return total

    def cd(self, goal):
        if goal == "..":
            return self.parent
        else:
            return [dir for dir in self.directories if dir.name == goal][0]

    def add_directory(self, directory):
        self.directories.append(directory)

    def add_file(self, file):
        self.files.append(file)

    def get_all_dir_sizes(self):
        sizes = []
        for dir in self.directories:
            sizes.append((dir.name, dir.size))
            sizes.extend(dir.get_all_dir_sizes())
        return sizes


def read_data(filename="input.txt"):
    COMMAND = "$"
    root = Directory("/", None)
    with open(filename) as file:
        current_directory = root
        for line in file.readlines():
            line = line.strip()
            if line.startswith(COMMAND):
                if "cd" in line and "cd /" not in line:
                    goal = line.split()[-1]
                    current_directory = current_directory.cd(goal)
            else:
                size, name = line.split(" ")
                if size == "dir":
                    directory = Directory(name, current_directory)
                    current_directory.add_directory(directory)

                else:
                    file = File(name, int(size))
                    current_directory.add_file(file)

    return root


def solve_1(data):
    # 9:12 to 10:03
    return data.size_lower


def solve_2(data):
    # 10:04 to 10:16
    SPACE_MAX = 70000000
    SPACE_UPDATE = 30000000
    SPACE_USED = data.size
    SPACE_UNUSED = SPACE_MAX - SPACE_USED
    SPACE_DELETE = SPACE_UPDATE - SPACE_UNUSED
    sizes = [size for size in data.get_all_dir_sizes() if size[1] >=
             SPACE_DELETE]
    sizes.sort(key=lambda x: x[1], reverse=True)
    return sizes[-1]


if __name__ == "__main__":
    data = read_data("input_test.txt")
    # pprint(data)
    print("Test part 1: ", solve_1(data))
    print("Test part 2: ", solve_2(data))

    data = read_data("input.txt")
    print("Real part 1: ", solve_1(data))
    print("Real part 2: ", solve_2(data))
