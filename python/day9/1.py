from tqdm import trange

with open("input") as f:
    line = f.read().strip()

disk = []
numbers = 0

for i, num in enumerate(line):
    if i % 2 == 0:
        disk.extend([str(i // 2)] * int(num))
        numbers += int(num)
    else:
        disk.extend(["."] * int(num))

r = len(disk) - 1
for i in trange(numbers):
    while disk[r] == ".":
        r -= 1
    if disk[i] == ".":
        disk[i], disk[r] = disk[r], disk[i]
        r -= 1

checksum = 0
for i, block in enumerate(disk):
    if block != ".":
        checksum += int(block) * i

print("".join(disk))
print(checksum)
