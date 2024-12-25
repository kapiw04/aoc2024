with open("input") as f:
    lines = f.readlines()

cells = [[int(c) for c in line.strip()] for line in lines]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
rows, cols = len(cells), len(cells[0])

path_counts = {
    # ex. (0, 0): 2 - from 0,0 we can reach to 9 ultimately in 2 ways
}

def get_adjacent_cells(x, y, height):
    adj = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < cols and 0 <= ny < rows and cells[ny][nx] == height + 1:
            adj.append((nx, ny))
    return adj

def populate_path_counts(height):
    for y in range(rows):
        for x in range(cols):
            if cells[y][x] == height:
                if height == 9:
                    path_counts[(x, y)] = 1
                else:
                    path_counts[(x, y)] = sum(path_counts.get((nx, ny), 0) 
                                              for nx, ny in get_adjacent_cells(x, y, height))

for h in range(9, -1, -1):
    populate_path_counts(h)

total_rating = 0
for y in range(rows):
    for x in range(cols):
        if cells[y][x] == 0:
            total_rating += path_counts.get((x, y), 0)

print(total_rating)
