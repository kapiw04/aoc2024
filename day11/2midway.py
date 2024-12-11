"""
https://i.etsystatic.com/30166514/r/il/58761d/3998512923/il_fullxfull.3998512923_k6jp.jpg
:)

I figured 0's are predictable, so I calculated the number of 0's for each iteration and added them to the final count.
Unfortunately this doesn't work as much quicker. I also tried to create a dict with known values in similar fashion to 
below solution but for any number, not just zeroes. Then I realised: order doesn't matter, just the count of each number. That's where
I stopped and decided to go with solution from 2.py.
"""

import math
from tqdm import trange

with open("input") as f:
    stones = f.read().split()
    stones = list(map(int, stones))

def calculate_for_0(iters):
    stones_arr = [0]
    for i in range(iters):
        length = len(stones_arr)
        for j in range(length):
            handle_stone(j, stones_arr, i)
        yield len(stones_arr)

def handle_stone(index, stones_arr, iteration):
    global additional
    if stones_arr[index] == 0:
        if iteration <= 29:
            stones_arr[index] = 1
        else:
            stones_arr.pop(index)
            additional += zeros[75-iteration]
        return  
        
    number_of_digits = int(math.log10(stones_arr[index]))+1
    if number_of_digits % 2 == 0:
        stone1 = stones_arr[index] // 10**(number_of_digits // 2)
        stone2 = stones_arr[index] % 10**(number_of_digits // 2)

        stones_arr[index] = stone1
        stones_arr.append(stone2)

    else:
        stones_arr[index] *= 2024


def blink(iteration):
    length = len(stones)
    for i in trange(length, desc=f"Blinking {iteration}"):  
        handle_stone(i, stones, iteration)

additional = 0

# for output in calculate_for_0(50):
#     with open("output", "a") as f:
#         f.write(str(output) + "\n")

with open("output") as f:
    zeros = f.read().split()
    zeros = list(map(int, zeros))

for i in trange(75, desc="Blinking"):
    blink(i)

print(len(stones) + additional)