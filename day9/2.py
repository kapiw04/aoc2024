from tqdm import tqdm

with open("input") as f:
    line = f.read().strip()

disk = []
files = []  # (file_id, start, length)
free_spaces = []  # (start, length)

pos = 0
for i, num in enumerate(line):
    size = int(num)
    if i % 2 == 0:
        file_id = i // 2
        disk.extend([str(file_id)] * size)
        files.append((file_id, pos, size))
    else:
        disk.extend(["."] * size)
        free_spaces.append((pos, size))
    pos += size

for file_id, file_start, file_length in tqdm(sorted(files, reverse=True)):
    for idx, (space_start, space_length) in enumerate(free_spaces):
        if space_length >= file_length and space_start < file_start:
            for i in range(file_length):
                disk[space_start + i] = str(file_id)
                disk[file_start + i] = "."
            
            if space_length == file_length:
                del free_spaces[idx]
            else:
                free_spaces[idx] = (space_start + file_length, space_length - file_length)

            free_spaces.append((file_start, file_length))
            break

checksum = sum(i * int(block) for i, block in enumerate(disk) if block != ".")
print(checksum)
