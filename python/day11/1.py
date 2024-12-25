from tqdm import trange

with open("input") as f:
    stones = f.read().split()
    stones = list(map(int, stones))

def handle_stone(index):
    number_of_digits = len(str(stones[index]))
    if stones[index] == 0:
        stones[index] = 1

    elif number_of_digits % 2 == 0:
        stone1 = stones[index] // 10**(number_of_digits // 2)
        stone2 = stones[index] % 10**(number_of_digits // 2)

        stones[index] = stone1
        stones.append(stone2)

    else:
        stones[index] *= 2024


def blink():
    length = len(stones)
    for i in range(length):
        handle_stone(i)

for i in trange(75):
    blink()

print(len(stones))