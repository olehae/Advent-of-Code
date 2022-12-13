from functools import cmp_to_key
from math import prod


def cmp(left, right):
    match left, right:
        case int(), int():
            return (left > right) - (left < right)
        case int(), list():
            return cmp([left], right)
        case list(), int():
            return cmp(left, [right])
        case list(), list():
            for z in map(cmp, left, right):
                if z:
                    return z
            return cmp(len(left), len(right))


packets = [[*map(eval, x.split())] for x in open('input13.txt').read().split('\n\n')]

print(cmp(*packets[0]))
for i in packets:
    print(i)

print(sum(i for i, p in enumerate(packets, 1) if cmp(*p) == -1))

packets = sorted(sum(packets, [[2], [6]]), key=cmp_to_key(cmp))
print(prod(i for i, p in enumerate(packets, 1) if p in [[2], [6]]))