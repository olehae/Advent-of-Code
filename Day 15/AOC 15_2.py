import z3

with open("input15.txt") as f:
    lines = f.readlines()

print(lines)
coords = []

for x in lines:
    new = x.replace("Sensor at x=", "(").replace(": closest beacon is at x=", "),(").replace("\n", ")").replace(" y=", "", 2)
    coords.append(eval(new))

print(coords)

s = z3.Solver()
x = z3.Int("x")
y = z3.Int("y")

s.add(0 <= x)
s.add(x <= 4000000)
s.add(0 <= y)
s.add(y <= 4000000)


def z3_abs(number):
    return z3.If(number >= 0, number, -number)  # Normal abs does not work within z3.Solver()


for i in coords:
    m = abs(i[0][0] - i[1][0]) + abs(i[0][1] - i[1][1])  # Distance from Sensor to Beacon
    s.add(z3_abs(i[0][0] - x) + z3_abs(i[0][1] - y) > m)  # we want to solve for x and y
    # -> they have to be out of range from every sensor
    # -> Distance from Sensor to Beacon closest to it has to be smaller than Distance from (x,y) to Sensor

assert s.check() == z3.sat  # Checks if s can be solved
model = s.model()

print(model[x].as_long() * 4000000 + model[y].as_long())  # solves model with all previously added conditions
