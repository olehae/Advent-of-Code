with open("input15.txt") as f:
    lines = f.readlines()

print(lines)
coords = []

for x in lines:
    new = x.replace("Sensor at x=", "(").replace(": closest beacon is at x=", "),(").replace("\n", ")").replace(" y=", "", 2)
    coords.append(eval(new))

print(coords)

given_y = 2000000
minim = coords[0][0][0]
maxim = coords[0][0][0]
beacons = []

for i in coords:
    x_distance = abs(i[0][0] - i[1][0])
    y_distance = abs(i[0][1] - i[1][1])
    distance = x_distance + y_distance

    if minim > i[0][0] - (distance - abs(i[0][1] - given_y)):
        minim = i[0][0] - (distance - abs(i[0][1] - given_y))
    if maxim < i[0][0] + (distance - abs(i[0][1] - given_y)):
        maxim = i[0][0] + (distance - abs(i[0][1] - given_y))
        print(minim, maxim)
    if i[1][1] == given_y and minim <= i[1][0] <= maxim:
        beacons.append(i[1][0])

print("\n", minim, maxim)

print(beacons)


print(maxim-minim+1-len(set(beacons)))