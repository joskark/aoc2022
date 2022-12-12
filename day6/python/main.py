from os import getcwd

path = getcwd()+"/input.txt"


def find_marker(line: str, n: int) -> int:
    count = 0
    end = count + n
    while end < len(line):
        s = set(line[count:end])
        if len(s) == n:
            return count + n
        count += 1
        end += 1


with open(path, encoding="utf-8") as f:
    line = f.read()
    print(f'Part 1: {find_marker(line, 4)}')
    print(f'Part 2: {find_marker(line, 14)}')
