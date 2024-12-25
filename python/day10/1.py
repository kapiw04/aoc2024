with open("example") as f:
    lines = f.readlines()

cells = [[int(c) for c in line if not c == "\n"] for line in lines]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

rows, cols = len(cells), len(cells[0])

def get_adjacent_cells(x, y, height):
    rows, cols = len(cells), len(cells[0])
    adj = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < cols and 0 <= ny < rows and cells[ny][nx] == height + 1:
            adj.append((nx, ny))
    return adj

def find_reachable_nines(x, y):
    if cells[y][x] == 9:
        return {(x, y)}
    reachable = set()
    for nx, ny in get_adjacent_cells(x, y, cells[y][x]):
        reachable |= find_reachable_nines(nx, ny)
    return reachable

total_score = 0
for y in range(rows):
    for x in range(cols):
        if cells[y][x] == 0:
            reachable_nines = find_reachable_nines(x, y)
            total_score += len(reachable_nines)

print(total_score)