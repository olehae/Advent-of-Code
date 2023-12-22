from collections import deque

with open('input22.txt') as f:
    lines = f.read().strip().split("\n")

bricks = []
for line in lines:
    s, e = line.split("~")
    s, e = list(map(int, s.split(","))), list(map(int, e.split(",")))
    bricks.append(list(s + e))

bricks.sort(key=lambda x: x[2])
print(bricks)


def blocked_below(above, below):
    # Look from above (ignore z) and check if two rectangles intersect
    x_intersect = max(above[0], below[0]) <= min(above[3], below[3])
    y_intersect = max(above[1], below[1]) <= min(above[4], below[4])
    return x_intersect and y_intersect


for i, brick in enumerate(bricks):
    min_z = 1
    for other_brick in bricks[:i]:
        if blocked_below(brick, other_brick):
            # brick[5] is always >= brick[2]
            min_z = max(min_z, other_brick[5] + 1)
    brick[5] -= brick[2] - min_z
    brick[2] = min_z

bricks.sort(key=lambda x: x[2])
n = len(bricks)
supports = {i: set() for i in range(n)}
is_supported_by = {i: set() for i in range(n)}

for i, below in enumerate(bricks):
    for j, above in enumerate(bricks[i+1:], start=i+1):
        if blocked_below(above, below) and above[2] - below[5] == 1:
            supports[i].add(j)
            is_supported_by[j].add(i)


out1 = 0
out2 = 0
for i in range(n):
    if all(len(is_supported_by[x]) >= 2 for x in supports[i]):
        out1 += 1

    q = deque(j for j in supports[i] if len(is_supported_by[j]) == 1)
    falls = set(q)
    falls.add(i)

    while q:
        j = q.popleft()
        for x in supports[j] - falls:
            if is_supported_by[x] <= falls:
                q.append(x)
                falls.add(x)

    out2 += len(falls) - 1

print(f"Part 1: {out1}")
print(f"Part 2: {out2}")
