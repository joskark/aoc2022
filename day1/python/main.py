import os

path = os.getcwd()+"/input.txt"

with open(path, encoding="utf-8") as f:
    lines = f.read().split("\n\n")
    for i in range(len(lines)):
        lines[i] = [int(x) for x in lines[i].split("\n")]

    sum_all = [sum(i) for i in lines]
    sum_all.sort()

    print(f"Part 1: {sum_all[-1]}")
    print(f"Part 2: {sum(sum_all[-3:])}")
