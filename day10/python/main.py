import os
from typing import List

input_path = os.getcwd()+"/input"


def part1(lines: List[str]) -> int:
    ranges = [20, 60, 100, 140, 180, 220]
    ans = []
    count = 0
    res = 1
    for line in lines:
        instruction = line[:4]
        if instruction == 'noop':
            count += 1
            if count in ranges:
                ans.append(res*count)
        else:
            value = int(line[5:])
            count += 1
            if count in ranges:
                ans.append(res*count)
            count += 1
            if count in ranges:
                ans.append(res*count)
            res += value
    return sum(ans)


def part2(lines: List[str]) -> List[List[str]]:
    sprite = ["#"]*3 + ["."]*37
    ans = [['.']*40 for i in range(6)]
    ranges = [40, 80, 120, 160, 200]
    index = 0
    cycles = 0
    registerX = 1
    for line in lines:
        instruction = line[:4]
        if instruction == 'noop':
            cycles += 1
            if cycles in ranges:
                index += 1
            ans[index][(cycles-1) % 40] = sprite[(cycles-1) % 40]
        else:
            value = int(line[5:])
            for i in range(2):
                cycles += 1
                if cycles in ranges:
                    index += 1
                ans[index][(cycles-1) % 40] = sprite[(cycles-1) % 40]
            registerX += value
            sprite = ["."]*40
            for i in range(registerX-1, registerX-1+3):
                if i >= 0 and i < 40:
                    sprite[i] = '#'

    return ans


with open(input_path, encoding="utf-8") as f:
    lines = f.read().split("\n")
    print(f"Part 1: {part1(lines)}")

    # part 2
    for i in part2(lines):
        print(''.join(i))
