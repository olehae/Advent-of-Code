import numpy as np

with open('input11.txt') as f:
    lines = f.read().strip().split("\n")

grid = np.array([list(line) for line in lines])


def distances(grid, factor):
    rows, cols = grid.shape
    empty_rows = [i for i in range(rows) if "#" not in grid[i, :]]
    empty_cols = [i for i in range(cols) if "#" not in grid[:, i]]

    galaxies = np.stack(np.where(grid == "#"), axis=1)
    out = 0
    for i, g1 in enumerate(galaxies):
        for g2 in galaxies[i+1:]:
            r_count = sum([g1[0] < x < g2[0] or g2[0] < x < g1[0] for x in empty_rows])
            c_count = sum([g1[1] < x < g2[1] or g2[1] < x < g1[1] for x in empty_cols])
            diff = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) + (r_count + c_count) * (factor-1)
            out += diff
    return out


print(f"Part 1: {distances(grid, 2)}")
print(f"Part 2: {distances(grid, 1000000)}")
