import os
from typing import List

input_path = os.getcwd()+"/input.txt"

subdirs = {}
direct_directory_size = {}


def create_tree(lines: List[str]) -> None:
    for line in lines:
        if line[0] == "$":
            ds, cmd, *ddir = line.split()
            if cmd == "cd":
                path = ddir[0]
                if path == "/":
                    curdir = path
                else:
                    curdir = os.path.normpath(os.path.join(curdir, path))
                if curdir not in subdirs:
                    subdirs[curdir] = []
                    direct_directory_size[curdir] = 0
        else:
            fsize, fname = line.split()
            if fsize != "dir":
                direct_directory_size[curdir] += int(fsize)
            else:
                subdirs[curdir].append(
                    os.path.normpath(os.path.join(curdir, fname)))


def compute_dirsize(dirname: str) -> int:
    dirsize = direct_directory_size[dirname]
    for i in subdirs[dirname]:
        if i in subdirs:
            dirsize += compute_dirsize(i)
    return dirsize


def part1() -> int:
    ans = 0
    for i in subdirs:
        dirsize = compute_dirsize(i)
        if dirsize <= 100000:
            ans += dirsize
    return ans


def part2() -> int:
    total_space = 70000000
    space_required = 30000000
    space_used = compute_dirsize("/")

    delete_this_directory = total_space
    for i in direct_directory_size:
        dirsize = compute_dirsize(i)
        if dirsize >= space_required - (total_space - space_used) and dirsize <= delete_this_directory:
            delete_this_directory = dirsize

    return delete_this_directory


with open(input_path, encoding="utf-8") as f:
    lines = f.read().split("\n")
    create_tree(lines)
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
