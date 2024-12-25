import sys

keys = []
locks = []


def classify_element(element):
    if element[0][0] == ".":
        keys.append(element)
    else:
        locks.append(element)


def to_list(element):
    return [sum([row[i] == "#" for row in element]) for i in range(5)]


for element in sys.stdin.read().split("\n\n"):
    cells = [[c for c in row] for row in element.splitlines()]
    classify_element(cells)

for _ in keys:
    key = keys.pop(0)
    sizes = to_list(key)
    keys.append(sizes)

for _ in locks:
    lock = locks.pop(0)
    sizes = to_list(lock)
    locks.append(sizes)


def try_key_to_lock(key, lock):
    for i in range(5):
        if key[i] + lock[i] > 7:
            return False
    return True


count = 0
for key in keys:
    for lock in locks:
        if try_key_to_lock(key, lock):
            count += 1

print(count)
