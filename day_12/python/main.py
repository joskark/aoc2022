import os
from typing import List
from collections import deque

input_path = os.getcwd()+"/input.txt"


def find_shortest(arr: List[List[str]], start: str, neighbor: str) -> int:
    ROWS = len(arr)
    COLS = len(arr[0])

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    q = deque([])
    for x in range(ROWS):
        for y in range(COLS):
            if arr[x][y] == start:
                for i, j in dirs:
                    if 0 <= x+i < ROWS and 0 <= y+j < COLS and arr[x+i][y+j] == neighbor:
                        q.appendleft([(x+i, y+j), 1])
                break

    visited = set()

    while q:
        position, step = q.popleft()
        if position not in visited:
            for xx, yy in dirs:
                new_x = position[0]+xx
                new_y = position[1]+yy
                if 0 <= new_x < ROWS and 0 <= new_y < COLS:
                    if arr[new_x][new_y] == 'E' and arr[position[0]][position[1]] == 'z':
                        return step+1
                    if ord('a') <= ord(arr[new_x][new_y]) <= ord(arr[position[0]][position[1]]) or ord(arr[new_x][new_y]) == ord(arr[position[0]][position[1]]) + 1:
                        q.append([(new_x, new_y), step+1])
        visited.add(position)


with open(input_path, encoding="utf-8") as f:
    lines = f.read().split("\n")
    arr = [list(line) for line in lines]
    print(f"Part 1: {find_shortest(arr, 'S', 'a')}")
    print(f"Part 2: {find_shortest(arr, 'a', 'b')}")
