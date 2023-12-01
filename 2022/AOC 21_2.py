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
    key, value = a.split(': ')
    if key == 'humn':
        continue
    if value.isdigit():
        s.add(getvar(key) == int(value))
        continue
    a, op, b = value.split()
    a = getvar(a)
    b = getvar(b)
    if key == 'root':
        s.add(a == b)
    else:
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
print(s.model()[variables['humn']])
