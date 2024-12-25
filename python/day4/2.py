with open("input") as f:
    lines = f.read().splitlines()

chars = [[i for i in line] for line in lines]

directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

def is_cross(i, j):
    corner_chars = [chars[i+x][j+y] for x, y in directions]

    if any(cc == "X" or cc == "A" for cc in corner_chars):
        return False

    if corner_chars[0] == corner_chars[3] or corner_chars[1] == corner_chars[2]:
        return False
    
    if corner_chars.count("M") != 2 or corner_chars.count("S") != 2:
        return False
    
    return True    



def is_mas_in_direction(i, j):
    if 1 <= i < len(chars) - 1 and 1 <= j < len(chars[0]) - 1:
        return is_cross(i, j)
    else:
        return False

found = []

total_count = 0
for i in range(len(chars)):
    for j in range(len(chars[i])):
        if chars[i][j] == "A":
            if is_mas_in_direction(i, j):
                total_count += 1
                found.append((i, j))

print(total_count)
