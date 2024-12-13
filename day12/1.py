with open("input") as file:
    grid = [list(line.strip()) for line in file]
visited = set()

def calc_area_perimeter(x, y):
    letter = grid[x][y]
    stack = [(x, y)]
    perimeter = 0
    area = 0

    while stack:
        cx, cy = stack.pop()
        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))
        area += 1
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
                perimeter += 1

            elif grid[nx][ny] != letter:
                perimeter += 1
            elif (nx, ny) not in visited:
                stack.append((nx, ny))

    return area, perimeter

cost = 0

for x in range(len(grid)):
    for y in range(len(grid[0])):
        if (x, y) in visited:
            continue
        area, perimeter = calc_area_perimeter(x, y)
        cost += area * perimeter

print(cost)
