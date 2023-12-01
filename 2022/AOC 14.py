with open("input14.txt") as f:
    objects = [i.strip().split(" -> ") for i in f.readlines()]

data = []

for i in objects:
    tempi = []
    for j in i:
        tempi.append(eval(j))
    data.append(tempi)

print(data)

# data = [[(498,4), (498,6), (496,6)], [(503,4), (502,4), (502,9), (494,9)]]


grid = [["."]*600 for i in range(191)]


for i in data:
    for j, elem in enumerate(i[:-1]):
        if elem[0] == i[j+1][0]:
            if elem[1] < i[j+1][1]:
                for x in range(elem[1], i[j + 1][1] + 1):
                    grid[x][elem[0]] = "#"
            elif i[j+1][1] < elem[1]:
                for x in range(i[j+1][1], elem[1]+1):
                    grid[x][elem[0]] = "#"

        elif elem[1] == i[j+1][1]:
            if elem[0] < i[j+1][0]:
                for y in range(elem[0], i[j+1][0]+1):
                    grid[elem[1]][y] = "#"
            elif elem[0] > i[j+1][0]:
                for y in range(i[j+1][0], elem[0]+1):
                    grid[elem[1]][y] = "#"

grid[0][500] = "+"

dropping = False


def move():
    current_index = [0, 500]
    while True:
        if grid[current_index[0]+1][current_index[1]] == ".":
            current_index[0] += 1
        elif grid[current_index[0]+1][current_index[1]] in ("#", "o"):
            if grid[current_index[0]+1][current_index[1]-1] == ".":
                current_index[0] += 1
                current_index[1] -= 1
            elif grid[current_index[0]+1][current_index[1]+1] == ".":
                current_index[0] += 1
                current_index[1] += 1
            else:
                grid[current_index[0]][current_index[1]] = "o"
                print(f"==={current_index}===")
                return False, 1
        if current_index[0] == len(grid)-1:
            break

    return True, 0


overall = 0
while not dropping:
    dropping, count = move()
    overall += count

for i in grid:
    for j in i[400:]:
        print(j, end="")
    print()

print(overall)

summe = 0

