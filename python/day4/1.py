with open("input") as f:
    lines = f.read().splitlines()

chars = [[i for i in line] for line in lines]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1),  # Up, Down, Left, Right
              (-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonal directions

def is_xmas_in_direction(i, j, dx, dy):
    word = "XMAS"
    x, y = i, j
    for char in word:
        if 0 <= x < len(chars) and 0 <= y < len(chars[0]) and chars[x][y] == char:
            x += dx
            y += dy
        else:
            return False
    return True

def find_xmas(i, j):
    count = 0
    for dx, dy in directions:
        if is_xmas_in_direction(i, j, dx, dy):
            count += 1
    return count

total_count = 0
for i in range(len(chars)):
    for j in range(len(chars[i])):
        if chars[i][j] == "X":
            total_count += find_xmas(i, j)

print(total_count)
