with open('input18.txt') as f:
    lines = f.read().strip().split("\n")

instructions = [x.split() for x in lines]

current1, current2 = (0, 0), (0, 0)
dug1, dug2 = [(0, 0)], [(0, 0)]
boundaries1, boundaries2 = 0, 0
dirs = {"U": (-1, 0), "L": (0, -1), "D": (1, 0), "R": (0, 1),
        "3": (-1, 0), "2": (0, -1), "1": (1, 0), "0": (0, 1)}
for direction, duration, hexa in instructions:
    # Part 1
    n1 = int(duration)
    i1, j1 = dirs[direction]
    current1 = (current1[0]+i1*n1, current1[1]+j1*n1)
    dug1.append(current1)
    boundaries1 += n1

    # Part 2
    n2 = int(hexa[2:-2], 16)
    i2, j2 = dirs[hexa[-2]]
    current2 = (current2[0] + i2 * n2, current2[1] + j2 * n2)
    dug2.append(current2)
    boundaries2 += n2


# Polygon area formula
A1 = abs(sum(dug1[i][0] * (dug1[(i-1) % len(dug1)][1] - dug1[(i+1) % len(dug1)][1]) for i in range(len(dug1)))) // 2
# Picks Theorem
interior1 = A1 - boundaries1 // 2 + 1
print(f"Part 1: {interior1 + boundaries1}")

# Polygon area formula
A2 = abs(sum(dug2[i][0] * (dug2[(i-1) % len(dug2)][1] - dug2[(i+1) % len(dug2)][1]) for i in range(len(dug2)))) // 2
# Picks Theorem
interior2 = A2 - boundaries2 // 2 + 1
print(f"Part 2: {interior2 + boundaries2}")
