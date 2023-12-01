with open("input14.txt") as f:
    objects = [i.strip().split(" -> ") for i in f.readlines()]

data = []

for i in objects:
    tempi = []
    for j in i:
        tempi.append(eval(j))
    data.append(tempi)

print(data)

for i in data:
    for j, elem in enumerate(i):
        i[j] = (i[j][0]+100, i[j][1])


grid = [["."]*800 for i in range(191)]

maxim = 0
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
        if elem[1] > maxim:
            maxim = elem[1]
        if i[j+1][1] > maxim:
            maxim = i[j+1][1]

for i, elem in enumerate(grid[157]):
    grid[159][i] = "#"

grid[0][600] = "+"

dropping = False


def move():
    current_index = [0, 600]
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
                if current_index == [0, 600]:
                    return True, 1
                else:
                    return False, 1





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
