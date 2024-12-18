import heapq
from utils import input_lines

ROWS = 71
COLS = 71

memory = [["." for _ in range(COLS)] for _ in range(ROWS)]

def find_path():
    for i, line in enumerate(input_lines("{int},{int}")):
        x, y = line
        memory[y][x] = "#"
        if i >= 1023:
            break

    dist = [[float("inf") for _ in range(COLS)] for _ in range(ROWS)]
    prev = [[None for _ in range(COLS)] for _ in range(ROWS)]

    dist[0][0] = 0
    pq = [(0, 0, 0, 0)]

    while pq:
        d, x, y, moves = heapq.heappop(pq)
        if x == COLS - 1 and y == ROWS - 1:
            break

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < COLS and 0 <= ny < ROWS and memory[ny][nx] == ".":
                if dist[ny][nx] > d + 1:
                    dist[ny][nx] = d + 1
                    prev[ny][nx] = (x, y)
                    heapq.heappush(pq, (d + 1, nx, ny, moves + 1))
                    
    print(dist[ROWS - 1][COLS - 1])

find_path()