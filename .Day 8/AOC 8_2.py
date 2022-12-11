with open("input8.txt") as f:
    lines = f.readlines()

print(f"{lines=}")

grid = []
for i in lines:
    grid.append(list(map(int, list(i.replace("\n", "")))))

print(f"{grid=}")


def right_score(index, liste):
    count = 0
    for x in liste[index+1:]:
        if x < liste[index]:
            count += 1
        else:
            count += 1
            break
    return count


def left_score(index, liste):
    count = 0
    for x in liste[:index][::-1]:
        if x < liste[index]:
            count += 1
        else:
            count += 1
            break
    return count


def down_score(index, liste):
    count = 0
    for x in [row[index] for row in grid][grid.index(liste)+1:]:
        if x < liste[index]:
            count += 1
        else:
            count += 1
            break
    return count


def up_score(index, liste):
    count = 0
    for x in [row[index] for row in grid][:grid.index(liste)][::-1]:
        if x < liste[index]:
            count += 1
        else:
            count += 1
            break
    return count


best_scenic_score = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        scenic_score = right_score(j, grid[i]) * left_score(j, grid[i]) * down_score(j, grid[i]) * up_score(j, grid[i])
        if best_scenic_score < scenic_score:
            best_scenic_score = scenic_score

print(f"\n{best_scenic_score=}")
