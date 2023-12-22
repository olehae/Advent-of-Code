from collections import deque

with open('input21.txt') as f:
    grid = [list(x) for x in f.read().strip().split("\n")]

m, n = len(grid), len(grid[0])
# m == n -> grid is quadratic

for i, g in enumerate(grid):
    try:
        s = (i, g.index("S"))
        break
    except ValueError:
        pass


def walk_grid(start, steps):
    visited = {(*start, 0)}
    current = {start}
    for step in range(1, steps+1):
        new = set()
        for i, j in current:
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni % m][nj % n] != "#" and (ni % m, nj % n, step) not in visited:
                    visited.add((ni % m, nj % n, step))
                    new.add((ni % m, nj % n))
        current = new.copy()

    """out = 0
    for i, j in current:
        grid[i][j] = "O"
    for g in grid:
        print("".join(g))"""

    return len(current)


print(f"Part 1: {walk_grid(s, 64)}")
