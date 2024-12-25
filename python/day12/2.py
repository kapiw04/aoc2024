from calendar import c
import collections


with open("input") as file:
    grid = [list(line.strip()) for line in file]

not_origins = set()


visited = set()

def calc_area_perimeter(x, y, visited):
    letter = grid[x][y]
    stack = collections.deque([(x, y)])
    perimeter = 0
    area = 0
    border_edges = collections.defaultdict(list)
    # border_edges = {(dx, dy, x or y): set of x or y (x if )}

    while stack:
        cx, cy = stack.pop()
        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))
        area += 1
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] != letter:
                if dx == 0:
                    border_edges[(dx, dy, ny)].append(nx)
                else:
                    border_edges[(dx, dy, nx)].append(ny)
            elif (nx, ny) not in visited:
                stack.append((nx, ny))

    for border_cells in border_edges.values():
        border_cells.sort()
        for i in range(1, len(border_cells)):
            if border_cells[i] - border_cells[i - 1] > 1:
                perimeter += 1

    return area, perimeter + len(border_edges)

cost = 0

for x in range(len(grid)):
    for y in range(len(grid[0])):
        if (x, y) not in visited:
            area, perimeter = calc_area_perimeter(x, y, visited)
            cost += area * perimeter

print(cost)
