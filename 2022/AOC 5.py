with open('input05.txt') as f:
    lines = f.readlines()

print(lines)

og_stack = lines[:lines.index('\n')-1]
instructions = lines[lines.index('\n')+1:]

stack = []
for i in og_stack[::-1]:
    counter = 1
    temp = []
    while counter < 34:
        temp.append(i[counter])
        counter += 4
    stack.append(temp)

print(f"{stack=}")

sorted_stack = [[],[],[],[],[],[],[],[],[]]

for i in stack:
    temp = 0
    for j in i:
        sorted_stack[temp].append(j)
        temp += 1

for i in sorted_stack:
    while " " in i:
        i.remove(" ")

print(f"{sorted_stack=}")

sorted_instructions = []
for i in instructions:
    sorted_instructions.append(i.replace("move ", "").replace("from ", "").replace("to ", "").replace("\n", ""))

print(f"{sorted_instructions=}")
instru_tup = []
for i in sorted_instructions:
    instru_tup.append(tuple(map(int, i.split(' '))))
print(f"{instru_tup=}")

for i in instru_tup:
    for j in range(i[0]):
        sorted_stack[i[2]-1].append(sorted_stack[i[1]-1].pop())

"""print(range(int(sorted_instructions[0][0])))
for i in range(int(sorted_instructions[0][0])):
    sorted_stack[5].append(sorted_stack[7].pop())"""
print(f"{sorted_stack=}")

for i in sorted_stack:
    print(i.pop(), end="")