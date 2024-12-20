from collections import Counter, defaultdict
import heapq
import sys

from tqdm import trange

rows = sys.stdin.readlines()
rows = list(map(str.strip, rows))

cells = [[c for c in row] for row in rows]
original = [[c for c in row] for row in rows]

path_cache = {}
def cached_find_shortest_path(cells, start, end):
    if (start, end) in path_cache:
        return path_cache[(start, end)]
    path = find_distances(cells, start, end)
    path_cache[(start, end)] = path
    return path


def find_distances(cells, source):
    costs = defaultdict(lambda: float('inf'))
    costs[source] = 0
    heap = [(0, source)]  # cost, position
    visited = set()

    while heap:
        cost, pos = heapq.heappop(heap)

        if pos in visited:
            continue
        visited.add(pos)

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = pos[0] + dx, pos[1] + dy
            if 0 <= nx < len(cells) and 0 <= ny < len(cells[0]) and cells[nx][ny] != '#':
                neighbor = (nx, ny)
                new_cost = cost + 1
                if new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    heapq.heappush(heap, (new_cost, neighbor))

    return costs


count = 0
p = []
start = next((x, y) for x, row in enumerate(cells) for y, val in enumerate(row) if val == 'S')
end = next((x, y) for x, row in enumerate(cells) for y, val in enumerate(row) if val == 'E')

from_start = find_distances(cells, start)
from_end = find_distances(cells, end)

no_cheating_path = from_start[end]
print(no_cheating_path)


for i in trange(len(cells)):
    for j in trange(len(cells[0])):
        cheat_cords = (i, j)
        to_cheat = from_start[cheat_cords]
        for dx in range(-20, 21):
            for dy in range(-20, 21):
                if abs(dx) + abs(dy) > 20 or (dx == 0 and dy == 0):
                    continue
                nx, ny = i + dx, j + dy
                if not (0 <= nx < len(cells) and 0 <= ny < len(cells[0])):
                    continue

                to_end = from_end[(nx, ny)]

                if to_cheat < float('inf') and to_end < float('inf'):
                    path = to_cheat + to_end + abs(dx) + abs(dy)
                    if no_cheating_path - path >= 100:
                        count += 1
                        p.append(no_cheating_path - path)

c = Counter(p)

for k, v in c.items():
    if k > 50:
        print(k, v) 

print(count)