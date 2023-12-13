import math

with open('input10.txt') as f:
    lines = f.read().strip().split("\n")

grid = [list(line) for line in lines]

for i, line in enumerate(grid):
    try:
        s = (i, line.index("S"))
        break
    except ValueError:
        pass


def find_next(last, current):
    i, j = current
    n, e, s, w = (-1, 0), (0, 1), (1, 0), (0, -1)
    pipes = {"|": [n, s], "-": [e, w], "L": [n, e], "J": [n, w], "7": [s, w], "F": [s, e]}
    dir1, dir2 = pipes[grid[i][j]]
    if (i+dir1[0], j+dir1[1]) == last:
        return i + dir2[0], j + dir2[1]
    elif (i+dir2[0], j+dir2[1]) == last:
        return i + dir1[0], j + dir1[1]
    else:
        return "Not Connected"


starts = []
for i, j in [(s[0], s[1]-1), (s[0], s[1]+1), (s[0]-1, s[1]), (s[0]+1, s[1])]:
    if grid[i][j] != "." and i >= 0 and j >= 0 and find_next(s, (i, j)) != "Not Connected":
        starts.append((i, j))

positions = {}
count = 1
last, current = s, starts[0]
while current != s:
    positions[current] = grid[current[0]][current[1]]
    last, current = current, find_next(last, current)
    count += 1

print(f"Part 1: {math.ceil(count/2)}")

form = {(-1, 0): {(0, 1): "L", (1, 0): "|", (0, -1): "J"},
        (0, 1): {(-1, 0): "L", (1, 0): "F", (0, -1): "-"},
        (1, 0): {(-1, 0): "|", (0, 1): "F", (0, -1): "7"},
        (0, -1): {(-1, 0): "J", (0, 1): "-", (1, 0): "7"}}

vis = grid.copy()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i, j) in positions:
            vis[i][j] = positions[(i, j)]
        elif (i, j) == s:
            f_1, f_2 = [(start[0]-s[0], start[1]-s[1]) for start in starts]
            vis[i][j] = form[f_1][f_2]
        else:
            vis[i][j] = "."

count = 0
for ax in ["i", "j"]:
    custom_range = range(len(vis)) if ax == "i" else range(1, len(vis[0]))
    for i_j in custom_range:
        crossed = 0
        i = i_j if ax == "i" else 0
        j = i_j if ax == "j" else 0
        while i < len(vis) and j < len(vis[0]):
            elem = vis[i][j]
            if elem in ["|", "-", "L", "J", "7", "F"]:
                if elem in ["L", "7"]:
                    crossed += 2
                else:
                    crossed += 1
            elif elem == "." and crossed % 2 == 1:
                count += 1
                vis[i][j] = "I"
            i += 1
            j += 1

print(f"Part 2: {count}")
