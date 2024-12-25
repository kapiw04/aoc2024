def is_safe(levels: list[int]):
    if levels != sorted(levels) and levels != sorted(levels, reverse=True):
        return False
    for i in range(1, len(levels)):
        if abs(levels[i] - levels[i - 1]) > 3 or abs(levels[i] - levels[i - 1]) < 1:
            return False
    return True


input = [levels for levels in open("/dev/stdin").read().splitlines()]

count = 0

for levels in input:
    levels = [int(level) for level in levels.split()]
    if is_safe(levels):
        count += 1
    else:
        print(levels)

print(count)
