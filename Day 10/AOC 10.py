with open("input10.txt") as f:
    data = f.readlines()

data = [i.replace("\n", "").split() for i in data]

print(f"\n{data=}\n")

x = 1
log = []
for i in range(len(data)):
    if data[i][0] == "noop":
        log.append(x)
    elif data[i][0] == "addx":
        log.append(x)
        log.append(x)
        x += int(data[i][1])

print(f"{log=}\n")

print(sum(log[i-1] * i for i in (20, 60, 100, 140, 180, 220)))

drawing = []

for i in range(240):
    if log[i]+1 >= i % 40 >= log[i]-1:
        drawing.append("██")
    else:
        drawing.append("░░")

print(f"\n{drawing=}\n")

for i in range(len(drawing)):
    print(drawing[i], end="")
    if i in (39, 79, 119, 159, 199):
        print()