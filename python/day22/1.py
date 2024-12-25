import sys

initials = list(sys.stdin)
initials = list(map(lambda x: int(x[:-1]), initials))

sys.setrecursionlimit(2500)


def get_secret(secret, iterations=2000):
    if iterations == 0:
        return secret

    def mix(x):
        return x ^ secret

    def prune(x):
        return x % 16777216

    secret = mix(secret * 64)
    secret = prune(secret)

    secret = mix(secret // 32)
    secret = prune(secret)

    secret = mix(secret * 2048)
    secret = prune(secret)

    return get_secret(secret, iterations - 1)


s = 0

for i in initials:
    s += get_secret(i)

print(s)
