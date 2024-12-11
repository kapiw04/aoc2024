import collections
import math
from tqdm import trange

with open("input") as f:
    stones = list(map(int, f.read().split()))

ITERATIONS = 75

def handle_stone(stone, count, new_counts):
    if stone == 0:
        new_counts[1] += count
    else:
        num_digits = math.ceil(math.log10(stone + 1))
        if num_digits % 2 == 0:
            half = num_digits // 2
            stone1 = stone // 10**half
            stone2 = stone % 10**half
            new_counts[stone1] += count
            new_counts[stone2] += count
        else:
            new_counts[stone * 2024] += count

def blink(current_counts):
    new_stone_counts = collections.defaultdict(int)
    for stone, count in current_counts.items():
        handle_stone(stone, count, new_stone_counts)
    return new_stone_counts

stone_counts = collections.defaultdict(int)
for stone in stones:
    stone_counts[stone] += 1

for _ in trange(ITERATIONS, desc="Blinking"):
    stone_counts = blink(stone_counts)

print(sum(stone_counts.values()))
