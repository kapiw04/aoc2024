import enum

with open("input") as f:
    rows = f.read().splitlines()

cells = [[i for i in row] for row in rows]

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

for y,row in enumerate(rows):
    x = row.find("^")
    if x != -1:
        current_pos = [x, y]
        break
        
def move(pos, direction):
    return [pos[0] + direction[0], pos[1] + direction[1]]

visited = set()
visited.add(tuple(current_pos))

while True:
    x = current_pos[0]
    y = current_pos[1]
    next_pos = move(current_pos, directions[facing])
    if next_pos[1] < 0 or next_pos[1] >= len(rows) or next_pos[0] < 0 or next_pos[0] >= len(rows[0]):
        break
    if rows[next_pos[1]][next_pos[0]] == "#":
        facing = turns[facing]
        continue
    current_pos = move(current_pos, directions[facing])
    visited.add(tuple(current_pos))

print(len(visited)) 
    # for i in range(len(cells)):
    #     for j in range(len(cells[i])):
    #         if (i, j) in visited:
    #             print("X", end="")
    #         else:
    #             print(cells[i][j], end="")
    #     print()