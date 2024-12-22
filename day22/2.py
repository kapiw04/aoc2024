import sys
from rich import print
import collections

initials = list(map(lambda x: int(x.strip()), sys.stdin))

counter: dict = collections.Counter()


def get_secret(secret, iterations=2000):
    window = []
    unique = set()

    for i in range(iterations):
        tmp = secret
        secret = (secret << 6) ^ secret
        secret &= 0xFFFFFF

        secret = (secret >> 5) ^ secret
        secret &= 0xFFFFFF

        secret = (secret << 11) ^ secret
        secret &= 0xFFFFFF

        change = secret % 10 - tmp % 10
        window.append(change)
        if len(window) >= 4:
            if tuple(window) not in unique:
                unique.add((tuple(window)))
                counter[tuple(window)] += secret % 10
            window.pop(0)


for initial in initials:
    get_secret(initial)

print(counter.most_common(1)[0][1])
# 2206 too low
# 2423 too high
