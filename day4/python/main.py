from os import getcwd
from typing import List

path = getcwd()+"/input.txt"


def char_number(character):
    if character.islower():
        return ord(character) - 96
    return ord(character) - 38


def part1(lines: List[str]) -> int:

    res = 0

    for line in lines:
        arr = [(x[0], x[1]) for x in (x.split("-") for x in line.split(","))]
        if (int(arr[0][0]) >= int(arr[1][0]) and int(arr[0][1]) <= int(arr[1][1])) or (int(arr[1][0]) >= int(arr[0][0]) and int(arr[1][1]) <= int(arr[0][1])):
            print(arr)
            res += 1

    return res


def part2(lines: List[str]) -> int:
    not_overlapping = 0

    for line in lines:
        arr = [(x[0], x[1]) for x in (x.split("-") for x in line.split(","))]
        if (int(arr[0][0]) > int(arr[1][1])) or (int(arr[0][1]) < int(arr[1][0])):
            not_overlapping += 1

    return len(lines) - not_overlapping


with open(path, encoding="utf-8") as f:
    lines = f.read().split("\n")
    print(f'Part 1: {part1(lines)}')
    print(f'Part 2: {part2(lines)}')
