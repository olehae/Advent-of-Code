with open("input08.txt") as f:
    lines = f.readlines()

print(f"{lines=}")

grid = []
for i in lines:
    grid.append(list(map(int, list(i.replace("\n", "")))))

print(f"{grid=}")

visible = 0
for i in range(len(grid)):
    if i == 0 or i == len(grid)-1:
        visible += len(grid[i])
    else:
        for j in range(len(grid[i])):
            if j == 0 or j == len(grid[i])-1:
                visible += 1
            else:
                if grid[i][j] > max(grid[i][:j]) or grid[i][j] > max(grid[i][j+1:]):
                    visible += 1
                elif grid[i][j] > max([row[j] for row in grid][:i]) or grid[i][j] > max([row[j] for row in grid][i+1:]):
                    visible += 1

print(f"\n{visible=}")
