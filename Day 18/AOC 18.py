with open("input18.txt") as f:
    data = f.readlines()

data = [tuple(map(int, i.replace("\n", "").split(","))) for i in data]

print(f"{data=}")


def compare(cube, cube_list):
    positions = [True, True, True, True, True, True]
    for i in cube_list:
        if i != cube:
            if cube[0] - i[0] == 1 and cube[1] == i[1] and cube[2] == i[2] and positions[0]:
                positions[0] = False
            elif cube[0] - i[0] == -1 and cube[1] == i[1] and cube[2] == i[2] and positions[1]:
                positions[1] = False
            elif cube[1] - i[1] == 1 and cube[0] == i[0] and cube[2] == i[2] and positions[2]:
                positions[2] = False
            elif cube[1] - i[1] == -1 and cube[0] == i[0] and cube[2] == i[2] and positions[3]:
                positions[3] = False
            elif cube[2] - i[2] == 1 and cube[0] == i[0] and cube[1] == i[1] and positions[4]:
                positions[4] = False
            elif cube[2] - i[2] == -1 and cube[0] == i[0] and cube[1] == i[1] and positions[5]:
                positions[5] = False
    return sum(i for i in positions if i)


print(sum(compare(i, data) for i in data))
