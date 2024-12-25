from collections import defaultdict
import heapq
import sys

from tqdm import trange

rows = sys.stdin.readlines()
rows = list(map(str.strip, rows))

cells = [[c for c in row] for row in rows]
directions = [
    (0, 1),  # right
    (1, 0),  # down
    (0, -1),  # left
    (-1, 0)  # up
]

def get_rotations(facing):
    idx = directions.index(facing)
    return [directions[(idx + 1) % len(directions)], directions[(idx - 1) % len(directions)]]

def find_distances(cells, source, source_facing=None):
    costs = defaultdict(lambda: float('inf'))
    if source_facing is None:
        heap = [(0, source, facing) for facing in directions]

        for facing in directions:
            costs[(source, facing)] = 0
    else:
        heap = [(0, source, source_facing)]
        costs[(source, source_facing)] = 0

    visited = set()

    while heap:
        cost, pos, facing = heapq.heappop(heap)
        if (pos, facing) in visited:
            continue
        visited.add((pos, facing))

        nx, ny = pos[0] + facing[0], pos[1] + facing[1]
        if 0 <= nx < len(cells) and 0 <= ny < len(cells[0]) and cells[nx][ny] != '#':
            neighbor = (nx, ny)
            new_cost = cost + 1
            if new_cost < costs[(neighbor, facing)]:
                costs[(neighbor, facing)] = new_cost
                heapq.heappush(heap, (new_cost, neighbor, facing))

        for new_facing in get_rotations(facing):
            nx, ny = pos[0] + new_facing[0], pos[1] + new_facing[1]
            if 0 <= nx < len(cells) and 0 <= ny < len(cells[0]) and cells[nx][ny] != '#':
                neighbor = (nx, ny)
                new_cost = cost + 1001
                if new_cost < costs[(neighbor, new_facing)]:
                    costs[(neighbor, new_facing)] = new_cost
                    heapq.heappush(heap, (new_cost, neighbor, new_facing))

    return costs


start = next((x, y) for x, row in enumerate(cells) for y, val in enumerate(row) if val == 'S')
end = next((x, y) for x, row in enumerate(cells) for y, val in enumerate(row) if val == 'E')

from_start = find_distances(cells, start, directions[0])
# for some reason only finds corners
from_end = find_distances(cells, end)

shortest_path = min(from_start.get((end, facing), float('inf')) for facing in directions)

valid = set()
for i in range(len(cells)):
    for j in range(len(cells[0])):
        if cells[i][j] == '#':
            continue
        dist_start = min(from_start.get(((i, j), facing), float('inf')) for facing in directions)
        dist_end = min(from_end.get(((i, j), facing), float('inf')) for facing in directions)

        if dist_start < float('inf') and dist_end < float('inf') and dist_start + dist_end == shortest_path:
            valid.add((i, j))

# for some reason finds anything BUT corners
from_end = find_distances(cells, end, directions[0])
for i in range(len(cells)):
    for j in range(len(cells[0])):
        if (i, j) in valid:
            continue
        if cells[i][j] == '#':
            continue
        dist_start = min(from_start.get(((i, j), facing), float('inf')) for facing in directions)
        dist_end = min(from_end.get(((i, j), facing), float('inf')) for facing in directions)

        if dist_start < float('inf') and dist_end < float('inf') and dist_start + dist_end == shortest_path:
            valid.add((i, j))


def draw_valids():
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            if (i, j) in valid:
                print('O', end='')
            else:
                print(cells[i][j], end='')
        print()

# draw_valids()
print(shortest_path)
print(len(valid))
