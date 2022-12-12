from os import getcwd
from typing import List
from copy import deepcopy

path = getcwd()+"/input.txt"
stacks = {
    1: ['D', 'T', 'R', 'B', 'J', 'L', 'W', 'G'],
    2: ['S', 'W', 'C'],
    3: ['R', 'Z', 'T', 'M'],
    4: ['D', 'T', 'C', 'H', 'S', 'P', 'V'],
    5: ['G', 'P', 'T', 'L', 'D', 'Z'],
    6: ['F', 'B', 'R', 'Z', 'J', 'Q', 'C', 'D'],
    7: ['S', 'B', 'D', 'J', 'M', 'F', 'T', 'R'],
    8: ['L', 'H', 'R', 'B', 'T', 'V', 'M'],
    9: ['Q', 'P', 'D', 'S', 'V']
}

stacks2 = deepcopy(stacks)


def part1(lines: List[str]) -> str:

    for line in lines:
        if len(line) and line[0] == 'm':
            new_line = line.split(' ')
            for i in range(int(new_line[1])):
                from_stack = int(new_line[3])
                to_stack = int(new_line[5])
                if len(stacks[from_stack]) > 0:
                    to_move = stacks[from_stack].pop()
                    stacks[to_stack].append(to_move)
    return ''.join([value[-1] for _, value in stacks.items()])


def part2(lines: List[str]) -> str:

    for line in lines:
        if len(line) and line[0] == 'm':
            new_line = line.split(' ')
            from_stack = int(new_line[3])
            to_stack = int(new_line[5])
            to_move = stacks2[from_stack][-int(new_line[1]):]
            stacks2[to_stack] += to_move
            stacks2[from_stack] = stacks2[from_stack][:-int(new_line[1])]
    return ''.join([value[-1] for _, value in stacks2.items()])


with open(path, encoding="utf-8") as f:
    lines = f.read().split("\n")
    print(f'Part 1: {part1(lines)}')
    print(f'Part 2: {part2(lines)}')
