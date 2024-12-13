import numpy as np

with open("input") as f:
    puzzles = f.read().split("\n\n")

for i, puzzle in enumerate(puzzles):
    puzzles[i] = [i for i in puzzle.split("\n")]

def solve_puzzle(puzzle: list[str]):
    # offsets
    a_x = puzzle[0].split(",")[0].split("+")[1]
    a_y = puzzle[0].split(",")[1].split("+")[1]
    b_x = puzzle[1].split(",")[0].split("+")[1]
    b_y = puzzle[1].split(",")[1].split("+")[1]

    out_x = puzzle[2].split(",")[0].split("=")[1]
    out_y = puzzle[2].split(",")[1].split("=")[1]

    v_a = np.array([int(a_x), int(a_y)])
    v_b = np.array([int(b_x), int(b_y)])

    v_out = np.array([int(out_x) + 10000000000000, int(out_y) + 10000000000000])

    coeffs = np.linalg.solve(np.stack((v_a, v_b)).T, v_out)

    if all(np.abs(coeffs - coeffs.round()) < 1e-3) and all(coeffs >= 0):
        coeffs = coeffs.round().astype(int)
        cost = 3 * coeffs[0] + coeffs[1]
        return cost
    return None

s = 0

for puzzle in puzzles:
    if sol := solve_puzzle(puzzle):
        s += sol


print(int(s))