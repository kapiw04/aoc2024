from os import wait
import sys
import time
# from rich import print

inp = sys.stdin.read().split("\n\n")

_map = [list(i) for i in inp[0].replace(".", "..").replace("O", "[]").replace("#", "##").replace("@", "@.").split("\n")]
# _map = [list(i) for i in inp[0].split("\n")]
moves = [i for line in inp[1].split("\n") for i in line]

directions = {
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0), 
    ">": (1, 0) 
}

def can_push(x, y, dx, dy):
    if _map[y][x] == ".":
        return True
    assert bracket_has_neighbour(x, y)
    # print_in_red(x, y)
    ch = _map[y][x]
    
    if ch == "[":
        bx, by = x + 1, y
    else:
        bx, by = x - 1, y

    nx, ny = x + 2*dx, y + dy
    nbx, nby = bx + 2*dx, by + dy

    if _map[ny][nx-dx] == "#" or _map[nby][nbx-dx] == "#":
        return False

    if dx == 0:
        if _map[ny][nx] == "." and _map[nby][nbx-dx] == ".":
            return True
        if _map[ny][nx] in "[]" or _map[nby][nbx-dx] in "[]":
            return can_push(nx, ny, dx, dy) and can_push(nbx, nby, dx, dy)
    if dx != 0:
        if _map[ny][nx] == ".":
            return True
        if _map[ny][nx] in "[]" or _map[nby][nbx] in "[]":
            return can_push(nx, ny, dx, dy) or can_push(nbx, nby, dx, dy)


    return False


def push_box(x, y, dx, dy):
    ch = _map[y][x]
    if not ch in "[]":
        return 
    nx, ny = x + 2*dx, y + dy
    nch = _map[ny][nx]
    if ch == "[":
        bx = x + 1
        by = y
    else:
        bx = x - 1
        by = y
    nbx, nby = bx + 2*dx, by + dy
    nbch = _map[nby][nbx]
    bch = _map[by][bx]
    if not _map[ny][nx] in ".[]":
        return 

    if nch in "[]" or nbch in "[]":
        if dx == 0:
            if nch in "[]":
                push_box(nx, ny, dx, dy)
            if nbch in "[]":
                push_box(nbx, nby, dx, dy)
        if dx != 0:
            if nbch in "[]":
                push_box(nx, ny, dx, dy)

    assert _map[ny][nx] == "."
    if dx != 0:
        _map[ny][nx-dx] = ch
        _map[nby][nbx-dx] = bch
        _map[y][x] = "."
    if dx == 0:
        _map[ny][nx] = ch
        _map[nby][nbx] = bch
        _map[y][x] = "."
        _map[by][bx] = "."
        
def check_order(x, y):
    if _map[y][x] == "[":
        return _map[y][x+1] == "]"
    if _map[y][x] == "]":
        return _map[y][x-1] == "["
    
def bracket_has_neighbour(x, y):
    if _map[y][x] == "[":
        return _map[y][x+1] == "]"
    if _map[y][x] == "]":
        return _map[y][x-1] == "["

def move(x, y):
    assert _map[y][x] == "@"
    dx, dy = directions[moves.pop(0)]
    nx, ny = x + dx, y + dy
    if _map[ny][nx] == "#":
        return x, y
    
    if _map[ny][nx] == ".":
        _map[ny][nx] = "@"
        _map[y][x] = "."
        return nx, ny

    if not can_push(nx, ny, dx, dy):
        return x, y
    global was_push

    if _map[ny][nx] in "[]":
        push_box(nx, ny, dx, dy)    
        was_push = True


    _map[ny][nx] = "@"
    _map[y][x] = "."
    return nx, ny



def print_map():
    if moves == []:
        return ""
    result = []
    for line in _map:
        for ch in line:
            if ch == "@":
                result.append("\033[91m@\033[0m")
                # result.append("@")
            else:
                result.append(ch)
        result.append("\n")
    print("".join(result))
    # clear screen
    time.sleep(0.2)
    print("\033[H\033[J")
    return "".join(result)


def print_in_red(x, y):
    for i, line in enumerate(_map):
        for j, ch in enumerate(line):
            if i == y and j == x:
                print(f"\033[91m{ch}\033[0m", end="")
            else:
                print(ch, end="")
        print()

iter = 0

print_map()

def part2():
    sx, sy = 0, 0
    for y in range(len(_map)):
        for x in range(len(_map[y])):
            if _map[y][x] == "@":
                break
        else:
            continue
        sx, sy = x, y
        break
    while moves:
        sx, sy = move(sx, sy)
        print_map()

part2()

s = 0

for i, line in enumerate(_map):
    for j, char in enumerate(line):
        if char == "[":
            s += 100*i + j

print(s)