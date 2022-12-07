with open('input7.txt') as f:
    lines = f.readlines()

print(lines)
formatted = []

for i in lines:
    formatted.append(i.replace("\n", ""))

print(formatted)