import os
from typing import List

input_path = os.getcwd()+"/input.txt"


def part1(arr: List[List[int]]) -> int:
    visible = 2*len(arr) + 2*len(arr[0]) - 4
    col_arr = []
    for row in range(len(arr)):
        col_arr.append([arr[x][row] for x in range(len(arr[0]))])
    for row in range(1, len(arr)-1):
        for col in range(1, len(arr[0])-1):
            if arr[row][col] > max(arr[row][:col]) or arr[row][col] > max(arr[row][col+1:]) or arr[row][col] > max(col_arr[col][:row]) or arr[row][col] > max(col_arr[col][row+1:]):
                visible += 1

    return visible


def part2(arr: List[List[int]]) -> int:
    res = 0
    col_arr = []
    # create array with columns to iterate
    for y in range(len(arr)):
        col_arr.append([arr[x][y] for x in range(len(arr[0]))])
    for row in range(1, len(arr)-1):
        for col in range(1, len(arr[0])-1):
            item = 1
            for count, value in enumerate(reversed(arr[row][:col])):
                if value >= arr[row][col]:
                    item *= (count+1)
                    break
            else:
                item *= len(arr[row][:col])
            for count, value in enumerate(reversed(col_arr[col][:row])):
                if value >= arr[row][col]:
                    item *= (count+1)
                    break
            else:
                item *= len(col_arr[col][:row])
            for count, value in enumerate(arr[row][col+1:]):
                if value >= arr[row][col]:
                    item *= (count+1)
                    break
            else:
                item *= len(arr[row][col+1:])
            for count, value in enumerate(col_arr[col][row+1:]):
                if value >= arr[row][col]:
                    item *= (count+1)
                    break
            else:
                item *= len(col_arr[col][row+1:])
            res = max(res, item)

    return res


with open(input_path, encoding="utf-8") as f:
    lines = f.read().split("\n")
    arr = [list(map(int, list(line))) for line in lines]
    print(f"Part 1: {part1(arr)}")
    print(f"Part 2: {part2(arr)}")
