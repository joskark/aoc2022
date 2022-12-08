from os import getcwd
from typing import List

path = getcwd()+"/input"


def char_number(character):
    if character.islower():
        return ord(character) - 96
    return ord(character) - 38


def part1(lines: List[str]) -> int:

    res = 0

    for line in lines:
        mid = len(line) // 2
        character = list(set(line[:mid]).intersection(line[mid:]))

        res += char_number(character[0])

    return res


def part2(lines: List[str]) -> int:
    res = 0

    for i in range(0, len(lines), 3):
        arr = [set(lines[i]), set(lines[i+1]), set(lines[i+2])]
        character = list(arr[0].intersection(*arr))

        res += char_number(character[0])

    return res


with open(path, encoding="utf-8") as f:
    lines = f.read().split("\n")
    print(f'Part 1: {part1(lines)}')
    print(f'Part 2: {part2(lines)}')
