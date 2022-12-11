import math
import typing
from dataclasses import dataclass, field
from functools import cached_property


@dataclass
class File:
    size: int


@dataclass
class Directory:
    identifier: int
    name: str
    parent: typing.Any
    files: list[File] = field(default_factory=list)
    children: list = field(default_factory=list)

    @cached_property
    def size(self):
        count = 0
        for file in self.files:
            count += file.size
        for directory in self.children:
            count += directory.size
        return count

    def __hash__(self):
        return self.identifier


class Calculator:
    def __init__(self, filename):
        dir_id = 0
        self.main_dir = Directory(parent=None, name='/', identifier=dir_id)
        current_dir = self.main_dir
        browsed_directories = [current_dir]

        with open(filename) as f:
            for line in f.readlines()[1:]:

                if line.startswith('$ ls'):
                    pass

                elif line.startswith('$ cd'):
                    if (change_dir_name := line.removeprefix('$ cd ').rstrip()) == '..':
                        current_dir = browsed_directories[browsed_directories.index(current_dir) - 1]
                    else:
                        for child in current_dir.children:
                            if child.name == change_dir_name:
                                current_dir = child
                                break
                    browsed_directories.append(current_dir)

                elif line.startswith('dir'):
                    new_dir_name = line.removeprefix('dir ').rstrip()
                    dir_id += 1
                    current_dir.children.append(Directory(parent=current_dir, name=new_dir_name, identifier=dir_id))

                else:
                    current_dir.files.append(File(size=int(line.split()[0])))

        self.directories = set(browsed_directories)

    def calculate_results(self):
        part1, part2 = 0, math.inf
        required_space = 30000000 - (70000000 - self.main_dir.size)

        for directory in self.directories:
            dir_size = directory.size
            if dir_size <= 100000:
                part1 += dir_size
            if required_space <= dir_size < part2:
                part2 = dir_size
        return part1, part2


calculator = Calculator("day_7.txt")
part1, part2 = calculator.calculate_results()
print(f'Result of part 1: "{part1}"')
print(f'Result of part 1: "{part2}"')
