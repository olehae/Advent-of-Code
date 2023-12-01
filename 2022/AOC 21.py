import z3

with open("input21.txt") as f:
    data = f.read()

s = z3.Solver()
variables = {}


def getvar(n):
    if n not in variables:
        variables[n] = z3.Int(n)
    return variables[n]


for a in data.splitlines():
    key, item = a.split(': ')

    if item.isdigit():
        s.add(getvar(key) == int(item))
        continue

    a, op, b = item.split()
    a = getvar(a)
    b = getvar(b)
    key = getvar(key)
    if op == '+':
        s.add(key == a + b)
    elif op == '-':
        s.add(key == a - b)
    elif op == '*':
        s.add(key == a * b)
    elif op == '/':
        s.add(key == a / b)
        s.add(a % b == 0)

s.check()

print(s.model()[variables['root']])
