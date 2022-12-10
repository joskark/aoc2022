import os
from typing import List

input_path = os.getcwd()+"/input"


def make_moves(moves: List[(int, int), int], rope_len: int) -> int:
    xs = [0] * rope_len
    ys = [0] * rope_len
    visited = {(xs[-1], ys[-1])}

    for (mx, my), distance in moves:
        for _ in range(distance):
            xs[0] += mx
            ys[0] += my
            for i in range(rope_len - 1):
                dx = xs[i + 1] - xs[i]
                dy = ys[i + 1] - ys[i]
                if abs(dx) == 2 or abs(dy) == 2:
                    xs[i+1] = xs[i] + int(dx / 2)
                    ys[i+1] = ys[i] + int(dy / 2)
            visited.add((xs[-1], ys[-1]))
    return len(visited)


with open(input_path, encoding="utf-8") as f:
    lines = f.read().split("\n")
    directions = {'L': (-1, 0), 'R': (1, 0), 'D': (0, -1), 'U': (0, 1)}
    moves = [(directions[line[0]], int(line[1:])) for line in lines]
    print(f"Part 1: {make_moves(moves, 2)}")
    print(f"Part 1: {make_moves(moves, 10)}")
