from collections import Counter

with open("input") as f:
    lines = [line.strip() for line in f]

counter = Counter("".join(lines))
freqs = {key for key, value in counter.items() if value >= 2 and key not in {".", "\n"}}

def find_positions(freq):
    positions = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == freq:
                positions.append((x, y))
    return positions

def calc_antinodes(f1, f2):
    dx, dy = f2[0] - f1[0], f2[1] - f1[1]
    an1 = (f1[0] - dx, f1[1] - dy)
    an2 = (f2[0] + dx, f2[1] + dy)
    return an1, an2

def verify_antinode(x, y):
    return 0 <= x < len(lines[0]) and 0 <= y < len(lines)

antinode_positions = set()

for freq in freqs:
    positions = find_positions(freq)
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            f1, f2 = positions[i], positions[j]
            an1, an2 = calc_antinodes(f1, f2)
            if verify_antinode(*an1):
                antinode_positions.add(an1)
            if verify_antinode(*an2):
                antinode_positions.add(an2)

print(len(antinode_positions))
