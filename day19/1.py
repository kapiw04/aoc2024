from functools import lru_cache
import sys

towels, patterns = sys.stdin.read().split("\n\n")

towels = set(towels.split(","))
towels = set([towel.strip() for towel in towels])
patterns = patterns.split("\n")

@lru_cache(maxsize=None)
def check_pattern(pattern):
    if pattern in towels:
        return True

    for i in range(1, len(pattern)):
        if check_pattern(pattern[:-i]) and check_pattern(pattern[-i:]):
            return True
    return False

count = 0

for pattern in patterns:
    if check_pattern(pattern):
        count += 1

print(count)
