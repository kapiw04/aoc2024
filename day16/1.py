from collections import defaultdict
import heapq
import sys

rows = sys.stdin.readlines()
rows = list(map(str.strip, rows))

cells = [[c for c in row] for row in rows]
directions = [
    (0, 1), # right
    (1, 0), # down
    (0, -1), # left 
    (-1, 0) # up
]

def get_rotations(facing):
    return [
        directions[(directions.index(facing) + 1) % len(directions)],
        directions[(directions.index(facing) - 1) % len(directions)]
    ]

costs = defaultdict(lambda: float('inf'))

start = next((x, y) for x, row in enumerate(cells) for y, val in enumerate(row) if val == 'S')
end = next((x, y) for x, row in enumerate(cells) for y, val in enumerate(row) if val == 'E')

facing = directions[0]
costs[(start, facing)] = 0
heap = [(0, start, facing)]  # cost, position, facing
visited = set()

assert cells[end[0]][end[1]] == 'E' and cells[start[0]][start[1]] == 'S'

while heap:
    cost, pos, facing = heapq.heappop(heap)

    if (pos, facing) in visited:
        continue

    visited.add((pos, facing))

    if pos == end:
        print(cost)
        break

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
