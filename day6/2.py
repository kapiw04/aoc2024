with open("input") as f:
    rows = f.read().splitlines()

directions = {
    "up": [0, -1],
    "right": [1, 0],
    "down": [0, 1],
    "left": [-1, 0],
}

turns = {
    "up": "right",
    "right": "down",
    "down": "left",
    "left": "up",
}

facing = "up"
current_pos = None
for y, row in enumerate(rows):
    x = row.find("^")
    if x != -1:
        current_pos = [x, y]
        break

starting_pos = current_pos.copy()

def move(pos, direction):
    return [pos[0] + direction[0], pos[1] + direction[1]]

count = 0

for i in range(len(rows)):
    for j in range(len(rows[i])):
        if (i, j) == (starting_pos[1], starting_pos[0]):
            continue

        temp_rows = [list(row) for row in rows]
        temp_rows[i][j] = "#"

        current_pos = starting_pos.copy()
        facing = "up"
        visited = set()
        visited.add((current_pos[0], current_pos[1], facing))

        while True:
            x, y = current_pos
            next_pos = move(current_pos, directions[facing])

            if (
                next_pos[1] < 0
                or next_pos[1] >= len(temp_rows)
                or next_pos[0] < 0
                or next_pos[0] >= len(temp_rows[0])
            ):
                break

            if temp_rows[next_pos[1]][next_pos[0]] == "#":
                facing = turns[facing]
                continue

            current_pos = next_pos

            state = (current_pos[0], current_pos[1], facing)
            if state in visited:
                count += 1
                break
            visited.add(state)

print(count)
