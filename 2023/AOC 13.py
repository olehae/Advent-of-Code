import numpy as np

with open('input13.txt') as f:
    lines = f.read().strip().split("\n\n")


def find_sep(grid, part):
    rows, cols = grid.shape
    for i, limit in enumerate([rows, cols]):
        for sep in range(1, limit):
            # Create starts and ends of the two intervals based on sep and limit
            if sep < limit/2:
                s, e = 0, sep*2
            elif sep > limit/2:
                s, e = sep-(limit-sep), limit
            else:
                s, e = 0, limit

            # i == 1 -> vertical sep, i == 0 -> horizontal sep
            if i:
                grid1 = grid[:, s:sep]
                grid2 = np.flip(grid[:, sep:e], axis=1)
                factor = 1
            else:
                grid1 = grid[s:sep, :]
                grid2 = np.flip(grid[sep:e, :], axis=0)
                factor = 100

            match part:
                case 1:
                    # Check if arrays are equal
                    if np.array_equal(grid1, grid2):
                        return sep * factor
                case 2:
                    # Check if arrays have one element that is different (smudge)
                    if len(np.where(grid1 != grid2)[0]) == 1:
                        return sep * factor


total1, total2 = 0, 0
for grid in lines:
    grid = np.array([list(g) for g in grid.split("\n")])
    total1 += find_sep(grid, 1)
    total2 += find_sep(grid, 2)

print(f"Part 1: {total1}")
print(f"Part 2: {total2}")
