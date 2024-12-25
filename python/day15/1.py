from __future__ import print_function
import re
import sys
import time

import os
import platform

if platform.system() == "Windows":
    os.system("pause")
else:
    os.system("/bin/bash -c 'read -s -n 1 -p \"Press any key to continue...\"'")
    print()

inp = sys.stdin.read().split("\n\n")

_map = [list(i) for i in inp[0].split("\n")]
moves = [i for line in inp[1].split("\n") for i in line]
         
directons = {
  "^": (0, -1),
  "v": (0, 1),
  "<": (-1, 0),
  ">": (1, 0)
}


def move(x, y):
    assert _map[y][x] == "@"
    dx, dy = directons[moves.pop(0)]
    nx, ny = x + dx, y + dy
    if _map[ny][nx] == "#":
        return x, y

    nnx, nny = nx, ny
    while _map[nny][nnx] != ".":
        nnx += dx
        nny += dy
        if _map[nny][nnx] == "#":
            return x, y

    if _map[ny][nx] == "O":
        _map[nny][nnx] = "O"

    _map[ny][nx] = "@"
    _map[y][x] = "."
    return nx, ny
        
sx, sy = 0, 0
for y in range(len(_map)):
    for x in range(len(_map[y])):
        if _map[y][x] == "@":
            break
    else:
        continue
    sx, sy = x, y
    break


def print_map():
    if moves == []:
        return
    print(f"### MOVE {moves[0]} ###")
    for line in _map:
        print("".join(line))
    # print("\033[H\033[J")

while moves:
    # print_map()
    sx, sy = move(sx, sy)
s = 0

for i, line in enumerate(_map):
    for j, char in enumerate(line):
        if char == "O":
            s += 100*i + j

print(s)