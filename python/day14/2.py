from collections import defaultdict

import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import utils 

input_format = "p={},{} v={},{}"
MAP_HEIGHT = 103
MAP_WIDTH = 101
SIMULATION_TIME = 10000000

robots_map = defaultdict(int)
robots_velocity = defaultdict(list[tuple[int, int]])

for field in utils.input_lines(input_format, default_func=int):
    x, y, vx, vy = field
    x %= MAP_WIDTH
    y %= MAP_HEIGHT
    robots_map[(x, y)] += 1
    robots_velocity[(x, y)].append((vx, vy))

for i in range(SIMULATION_TIME):
    positions = list(robots_map.keys())
    new_robots_velocity = defaultdict(list[tuple[int, int]])
    new_robots_map = defaultdict(int)
    all_separated = True

    for (x, y), velocities in robots_velocity.items():
        all_separated &= robots_map[(x, y)] == 1 
        for vx, vy in velocities:
            new_x = (x + vx) % MAP_WIDTH
            new_y = (y + vy) % MAP_HEIGHT
            
            new_robots_map[(new_x, new_y)] += 1
            new_robots_velocity[(new_x, new_y)].append((vx, vy))
    
    if all_separated:
        print(i)
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                print(robots_map.get((x,y), "."), end="")
            print()
        break

    robots_map = new_robots_map
    robots_velocity = new_robots_velocity

