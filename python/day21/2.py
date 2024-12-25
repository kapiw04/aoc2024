from functools import cache, lru_cache, partial
from itertools import permutations
import sys
from rich import print

sys.path.append("/".join(__file__.split("/")[:-2]))
import python.utils as utils

codes = [code[0] for code in utils.input_lines("{}")]

num_keypad = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "0": (1, 3),
    "A": (2, 3),
}

dir_keypad = {"^": (1, 0), "v": (1, 1), "<": (0, 1), ">": (2, 1), "A": (2, 0)}

movements = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}


def check_valid_permutation(permutation, keypad, current_position):
    temp_x, temp_y = current_position
    for move in permutation:
        dx, dy = movements[move]
        temp_x += dx
        temp_y += dy
        if (temp_x, temp_y) not in keypad.values():
            return False
    return True


@cache
def code_on_keypad(code, depth, keypad_items, current_position=None):
    keypad = dict(keypad_items)

    if not code:
        return 0
    if not current_position:
        current_position = keypad["A"]

    current_x, current_y = current_position
    target_x, target_y = keypad[code[0]]
    dx, dy = target_x - current_x, target_y - current_y

    move_sequence = []
    if dx > 0:
        move_sequence += [">"] * dx
    elif dx < 0:
        move_sequence += ["<"] * abs(dx)
    if dy > 0:
        move_sequence += ["v"] * dy
    elif dy < 0:
        move_sequence += ["^"] * abs(dy)

    if depth == 0:
        return (
            len(move_sequence)
            + code_on_keypad(code[1:], depth, keypad_items, (target_x, target_y))
            + 1
        )

    permutation_lengths = []
    for permutation in set(permutations(move_sequence)):
        if not check_valid_permutation(permutation, keypad, current_position):
            continue
        permutation_lengths.append(
            code_on_directional(tuple(list(permutation) + ["A"]), depth - 1)
        )
    length = min(permutation_lengths)

    return length + code_on_keypad(code[1:], depth, keypad_items, (target_x, target_y))


code_on_directional = partial(code_on_keypad, keypad_items=tuple(dir_keypad.items()))
code_on_num = partial(code_on_keypad, keypad_items=tuple(num_keypad.items()))

s = 0

for code in codes:
    result = code_on_num(code, 25)
    s += result * int(code[:-1])

print(s)
