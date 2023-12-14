import numpy as np

with open('input14.txt') as f:
    lines = f.read().strip().split("\n")


def cycle(grid, part2):
    if part2:
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    else:
        dirs = [(-1, 0)]
    for i_dir, j_dir in dirs:
        sorted_i_j = zip(*np.stack(np.where(grid == "O")))
        match (i_dir, j_dir):
            case (-1, 0):
                sorted_i_j = sorted(sorted_i_j, key=lambda x: x[0], reverse=False)
            case (0, -1):
                sorted_i_j = sorted(sorted_i_j, key=lambda x: x[1], reverse=False)
            case (1, 0):
                sorted_i_j = sorted(sorted_i_j, key=lambda x: x[0], reverse=True)
            case (0, 1):
                sorted_i_j = sorted(sorted_i_j, key=lambda x: x[1], reverse=True)

        for i, j in sorted_i_j:
            while len(grid) > i+i_dir >= 0 and len(grid[0]) > j+j_dir >= 0 and grid[i+i_dir][j+j_dir] == ".":
                grid[i][j] = "."
                grid[i+i_dir][j+j_dir] = "O"
                i, j, = i+i_dir, j+j_dir
    return grid


grid = cycle(np.array([list(line) for line in lines]), part2=False)
print(f"Part 1: {sum(np.count_nonzero(row == 'O') * (len(grid)-i) for i, row in enumerate(grid))}")

grid = np.array([list(line) for line in lines])
previous = []
for count in range(1000000000):
    grid = cycle(grid, part2=True)
    flattened = list(np.copy(grid).flatten())
    if flattened in previous:
        idx = previous.index(flattened)
        # print(f"Cycle {count+1} is same as Cycle {idx+1}")
        remaining = (1000000000-(count+1)) % (count-idx)
        break
    previous.append(flattened)
for _ in range(remaining):
    grid = cycle(grid, part2=True)

print(f"Part 2: {sum(np.count_nonzero(row == 'O') * (len(grid)-i) for i, row in enumerate(grid))}")
