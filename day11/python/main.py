import os
from typing import List
from copy import deepcopy

import sys
sys.set_int_max_str_digits(0)

input_path = os.getcwd()+"/input"

monkeys = {}


def create_structure(blocks: List[str]) -> dict:
    monkeys = {}
    for monkey in blocks:
        lines = [x.strip() for x in monkey.split('\n')]
        items_str = lines[1].split(':')
        items = [int(x.strip()) for x in items_str[-1].split(',')]

        operations_str = lines[2].split(':')
        operations_exp = [x for x in operations_str[-1].split('=')]
        operations = [x.strip() for x in operations_exp[-1].split()]

        divider = int(lines[3].split()[-1])
        div_success = lines[4][-1]
        div_fail = lines[5][-1]
        monkeys[lines[0][-2]] = {'items': items,
                                 'operations': operations,
                                 'divider': divider,
                                 'div_success': div_success,
                                 'div_fail': div_fail,
                                 'inspections': 0
                                 }

    return monkeys


def calc_worry(operation: List[str], item: int) -> int:
    first = item if operation[0] == 'old' else int(operation[0])
    second = item if operation[-1] == 'old' else int(operation[-1])
    if operation[1] == '*':
        return first * second
    else:
        return first + second


def find_part2_modulo(monkeys: dict) -> int:
    # For part2 a modulo is needed with result of the multiplication of
    # all dividers from each monkey.
    res = 1
    for i in monkeys:
        res *= monkeys[i]['divider']
    return res


def solve(monkeys: dict, iterations: int, part: str) -> int:
    res = []
    part2_modulo = find_part2_modulo(monkeys)
    for i in range(iterations):
        for monkey in monkeys:
            while monkeys[monkey]['items']:
                item = monkeys[monkey]['items'].pop(0)
                worry = calc_worry(monkeys[monkey]['operations'], item)
                bored_value = worry
                if part == 'part1':
                    bored_value = worry // 3
                elif part == 'part2':
                    bored_value = worry % part2_modulo
                move_to = monkeys[monkey]['div_success'] if bored_value % monkeys[
                    monkey]['divider'] == 0 else monkeys[monkey]['div_fail']
                monkeys[move_to]['items'].append(bored_value)
                monkeys[monkey]['inspections'] += 1

    for i in monkeys:
        res.append(monkeys[i]['inspections'])

    res.sort()

    return res[-1] * res[-2]


with open(input_path, encoding="utf-8") as f:
    blocks = f.read().split("\n\n")
    monkeys = create_structure(blocks)
    monkeys_copy = deepcopy(monkeys)
    print(f"Part 1: {solve(monkeys, 20, 'part1')}")
    print(f"Part 2: {solve(monkeys_copy, 10000, 'part2')}")
