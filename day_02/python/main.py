import os

path = os.getcwd()+"/input.txt"

d = {'A': 'X', 'B': 'Y', 'C': 'Z'}
d_points = {'X': 1, 'Y': 2, 'Z': 3}
d_score = {'win': 6, 'draw': 3, 'loss': 0}

d_points_2 = {'A': 1, 'B': 2, 'C': 3}
d_score_2 = {'Z': d_score['win'], 'Y': d_score['draw'], 'X': d_score['loss']}


def compare(pl1, pl2):
    if d[pl1] == pl2:
        return d_score['draw']
    if pl2 == 'X':
        if d[pl1] == 'Z':
            return d_score['win']
        elif d[pl1] == 'Y':
            return d_score['loss']
    if pl2 == 'Z':
        if d[pl1] == 'X':
            return d_score['loss']
        elif d[pl1] == 'Y':
            return d_score['win']
    if pl2 == 'Y':
        if d[pl1] == 'X':
            return d_score['win']
        elif d[pl1] == 'Z':
            return d_score['loss']


def to_win(pl1, result):
    if result == 'Y':
        return d_points_2[pl1]
    if result == 'X':
        if pl1 == 'A':
            return d_points_2['C']
        elif pl1 == 'B':
            return d_points_2['A']
        elif pl1 == 'C':
            return d_points_2['B']
    if result == 'Z':
        if pl1 == 'A':
            return d_points_2['B']
        elif pl1 == 'B':
            return d_points_2['C']
        elif pl1 == 'C':
            return d_points_2['A']


with open(path, encoding="utf-8") as f:
    lines = f.read().split("\n")

    res = 0
    res_2 = 0

    for line in lines:
        pl2 = line[-1]
        pl1 = line[0]
        res += d_points[pl2]
        res += compare(pl1, pl2)

        game_result = line[-1]
        res_2 += d_score_2[game_result]
        res_2 += to_win(pl1, game_result)

    print(f'Part 1: {res}')

    print(f'Part 2: {res_2}')
