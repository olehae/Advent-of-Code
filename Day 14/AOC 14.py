import numpy as np

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


grid = [["."]*600 for i in range(200)]


for i in data:
    for j, elem in enumerate(i[:-1]):
        if elem[0] == i[j+1][0]:
            for x in range(elem[1], i[j+1][1]+1):
                grid[x][elem[0]] = "#"

        elif elem[1] == i[j+1][1]:
            if elem[0] < i[j+1][0]:
                for y in range(elem[0], i[j+1][0]):
                    grid[elem[1]][y] = "#"
            elif elem[0] > i[j+1][0]:
                for y in range(i[j+1][0], elem[0]+1):
                    grid[elem[1]][y] = "#"



for i in grid:
    for j in i[400:]:
        print(j, end="")
    print()
