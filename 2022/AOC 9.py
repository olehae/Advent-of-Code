with open("input09.txt") as f:
    data = f.readlines()

data = [i.replace("\n", "").split() for i in data]

print(f"{data=}\n")

grid = [[0]*600 for i in range(600)]


def move_head(thing, direction):
    new_x = thing[0]
    new_y = thing[1]
    if direction == "U":
        new_y -= 1
    elif direction == "D":
        new_y += 1
    elif direction == "L":
        new_x += 1
    elif direction == "R":
        new_x -= 1

    return new_x, new_y


def move_tail(tail_cords, head_cords):
    new_x = tail_cords[0]
    new_y = tail_cords[1]
    if head_cords[0] - tail_cords[0] == 2:
        new_x += 1
        if head_cords[1] - tail_cords[1] in (1, 2):
            new_y += 1
        elif head_cords[1] - tail_cords[1] in (-1, -2):
            new_y -= 1
    elif head_cords[0] - tail_cords[0] == -2:
        new_x -= 1
        if head_cords[1] - tail_cords[1] in (1, 2):
            new_y += 1
        elif head_cords[1] - tail_cords[1] in (-1, -2):
            new_y -= 1
    elif head_cords[1] - tail_cords[1] == 2:
        new_y += 1
        if head_cords[0] - tail_cords[0] in (1, 2):
            new_x += 1
        elif head_cords[0] - tail_cords[0] in (-1, -2):
            new_x -= 1
    elif head_cords[1] - tail_cords[1] == -2:
        new_y -= 1
        if head_cords[0] - tail_cords[0] in (1, 2):
            new_x += 1
        elif head_cords[0] - tail_cords[0] in (-1, -2):
            new_x -= 1

    return new_x, new_y


head = (300, 300)
tail1 = tail2 = tail3 = tail4 = tail5 = tail6 = tail7 = tail8 = tail9 = (300, 300)

for i in data:
    for j in range(int(i[1])):
        head = move_head(head, i[0])
        tail1 = move_tail(tail1, head)
        tail2 = move_tail(tail2, tail1)
        tail3 = move_tail(tail3, tail2)
        tail4 = move_tail(tail4, tail3)
        tail5 = move_tail(tail5, tail4)
        tail6 = move_tail(tail6, tail5)
        tail7 = move_tail(tail7, tail6)
        tail8 = move_tail(tail8, tail7)
        tail9 = move_tail(tail9, tail8)

        grid[tail9[0]][tail9[1]] = " "  # change the tail you want to show here (in this case you get the sum of tail9)

for i in grid:
    for j in i:
        print(j, end="")
    print()

summe = 0
for i in grid:
    for j in i:
        if j == " ":
            summe += 1

print(f"{summe=}")
