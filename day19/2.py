from functools import lru_cache
import sys

towels, patterns = sys.stdin.read().strip().split("\n\n")
towels = {towel.strip() for towel in towels.split(",")}
patterns = [pattern.strip() for pattern in patterns.split("\n")]

split_counts = {}

@lru_cache
def check_pattern(pattern):
    if pattern in towels:
        return True

    for i in range(1, len(pattern)):
        if check_pattern(pattern[:-i]) and check_pattern(pattern[-i:]):
            return True
    return False
  
@lru_cache
def count_patterns(pattern):
    if pattern == "":
        return 1
    count = 0
    for towel in towels:
        if pattern.startswith(towel):
            count += count_patterns(pattern[len(towel):])
    return count
                
count = 0

for pattern in patterns:
    count += count_patterns(pattern)
    
print(count)