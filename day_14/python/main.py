import os

input_path = os.getcwd()+"/input.txt"

filled_arr = set()


def create_structure(lines):
    for line in lines:

        coordinates = []

        for str_coord in line.split(" -> "):
            x, y = map(int, str_coord.split(","))
            coordinates.append((x, y))

        for i in range(1, len(coordinates)):
            cx, cy = coordinates[i]
            px, py = coordinates[i - 1]

            if cy != py:
                assert cx == px
                for y in range(min(cy, py), max(cy, py) + 1):
                    filled_arr.add((cx, y))

            if cx != px:
                assert cy == py
                for x in range(min(cx, px), max(cx, px) + 1):
                    filled_arr.add((x, cy))

    max_y = max([coord[1] for coord in filled_arr])
    return max_y


def simulate_sand_part_1(filled_arr):
    x, y = 500, 0

    while y <= max_y:
        if (x, y + 1) not in filled_arr:
            y += 1
            continue

        if (x - 1, y + 1) not in filled_arr:
            x -= 1
            y += 1
            continue

        if (x + 1, y + 1) not in filled_arr:
            x += 1
            y += 1
            continue

        filled_arr.add((x, y))
        return True

    return False


def simulate_sand_part_2(filled_arr):
    x, y = 500, 0

    if (x, y) in filled_arr:
        return (x, y)

    while y <= max_y:
        if (x, y + 1) not in filled_arr:
            y += 1
            continue

        if (x - 1, y + 1) not in filled_arr:
            x -= 1
            y += 1
            continue

        if (x + 1, y + 1) not in filled_arr:
            x += 1
            y += 1
            continue

        break

    return (x, y)


def part1(filled_arr):
    ans = 0

    while True:
        res = simulate_sand_part_1(filled_arr)

        if not res:
            break

        ans += 1
    return ans


def part2(filled_arr):
    ans = 0

    while True:
        x, y = simulate_sand_part_2(filled_arr)
        filled_arr.add((x, y))
        ans += 1

        if (x, y) == (500, 0):
            break

    return ans


with open(input_path, encoding="utf-8") as f:
    lines = f.read().strip().split("\n")
    max_y = create_structure(lines)
    print(f"Part 1: {part1(filled_arr)}")
    print(f"Part 2: {part2(filled_arr)}")
