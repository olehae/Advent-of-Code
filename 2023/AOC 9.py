with open('input09.txt') as f:
    lines = f.read().strip().split("\n")

out1 = 0
out2 = 0
for line in lines:
    current = list(map(int, line.split()))
    below = [current.copy()]
    while not all(x == 0 for x in current):
        for i in range(len(current)-1):
            current[i] = current[i+1] - current[i]
        current.pop()
        below.append(current.copy())
    val1, val2 = 0, 0
    for i in range(len(below)-2, -1, -1):
        val1 += below[i][-1]
        val2 = below[i][0] - val2
    out1 += val1
    out2 += val2

print(f"Part 1: {out1}")
print(f"Part 2: {out2}")
