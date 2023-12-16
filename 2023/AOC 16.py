import numpy as np
from collections import deque

with open('input16.txt') as f:
    lines = f.read().strip().split("\n")


def energized(grid, pos_dir):
    m, n = grid.shape
    seen = set()
    q = deque([pos_dir])
    while q:
        i, j, id, jd = q.pop()
        ni, nj = i+id, j+jd
        if not (m > ni >= 0 and n > nj >= 0):
            continue
        if (ni, nj, id, jd) in seen:
            continue
        seen.add((ni, nj, id, jd))
        curr = grid[ni, nj]
        match curr:
            case "/":
                id, jd = -jd, -id
            case "\\":
                id, jd = jd, id
            case "-":
                if id != 0:
                    id, jd = 0, 1
                    q.append([ni, nj, 0, -1])
            case "|":
                if jd != 0:
                    id, jd = 1, 0
                    q.append([ni, nj, -1, 0])
        q.append([ni, nj, id, jd])

    return len(set(x[:2] for x in seen))


grid = np.array([list(l) for l in lines])

print(f"Part 1: {energized(grid, (0, -1, 0, 1))}")

m, n = grid.shape
out = 0
for i in range(m):
    out = max(out, energized(grid, (i, -1, 0, 1)))
    out = max(out, energized(grid, (i, n, 0, -1)))
for j in range(n):
    out = max(out, energized(grid, (-1, j, 1, 0)))
    out = max(out, energized(grid, (m, j, -1, 0)))

print(f"Part 2: {out}")
