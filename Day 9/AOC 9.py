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
        if head_cords[1] - tail_cords[1] == 1:
            new_y += 1
        elif head_cords[1] - tail_cords[1] == -1:
            new_y -= 1
    elif head_cords[0] - tail_cords[0] == -2:
        new_x -= 1
        if head_cords[1] - tail_cords[1] == 1:
            new_y += 1
        elif head_cords[1] - tail_cords[1] == -1:
            new_y -= 1
    elif head_cords[1] - tail_cords[1] == 2:
        new_y += 1
        if head_cords[0] - tail_cords[0] == 1:
            new_x += 1
        elif head_cords[0] - tail_cords[0] == -1:
            new_x -= 1
    elif head_cords[1] - tail_cords[1] == -2:
        new_y -= 1
        if head_cords[0] - tail_cords[0] == 1:
            new_x += 1
        elif head_cords[0] - tail_cords[0] == -1:
            new_x -= 1

    return new_x, new_y


head = (300, 300)
tail = (300, 300)

for i in data:
    for j in range(int(i[1])):
        head = move_head(head, i[0])
        tail = move_tail(tail, head)
        grid[tail[0]][tail[1]] = " "

"""for i in grid:
    for j in i:
        print(j, end="")
    print()"""

summe = 0
for i in grid:
    for j in i:
        if j == " ":
            summe += 1

print(f"{summe=}")
