import os
from functools import cmp_to_key

input_path = os.getcwd()+"/input.txt"


def compare_packets(left, right):
    if type(left) == list and type(right) == int:
        right = [right]

    if type(left) == int and type(right) == list:
        left = [left]

    if type(left) == int and type(right) == int:
        if left < right:
            return 1
        if left == right:
            return 0
        return -1

    if type(left) == list and type(right) == list:
        index = 0
        while index < len(left) and index < len(right):
            res = compare_packets(left[index], right[index])
            if res == 1:
                return 1
            if res == -1:
                return -1

            index += 1

        if index == len(left):
            if len(left) == len(right):
                return 0
            return 1

        return -1


def part1(lines: str) -> int:
    pairs = [[eval(x) for x in pair.split("\n")]
             for pair in lines.split("\n\n")]

    ans = 0

    for index, block in enumerate(pairs):
        left, right = block[0], block[1]
        if compare_packets(left, right) == 1:
            ans += index + 1

    return ans


def part2(lines: str) -> int:
    pairs = lines.replace("\n\n", "\n").split("\n")
    packets = [eval(x) for x in pairs]
    packets.append([[2]])
    packets.append([[6]])
    sorted_packets = sorted(packets, key=cmp_to_key(
        compare_packets), reverse=True)

    for index, packet in enumerate(sorted_packets):
        if packet == [[2]]:
            left = index + 1
        if packet == [[6]]:
            right = index + 1

    return left * right


with open(input_path, encoding="utf-8") as f:
    lines = f.read().strip()
    print(f"Part 1: {part1(lines)}")
    print(f"Part 2: {part2(lines)}")
