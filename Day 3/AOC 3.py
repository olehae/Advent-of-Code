import string

with open('input03.txt') as f:
    lines = f.readlines()

print(lines)
formatted = []
for i in lines:
    temp = []
    for j in i:
        if j != "\n":
            temp.append(j)
    formatted.append(temp)
print(f"\n{formatted=}")


doubles = []
for i in formatted:
    fhalf = i[:len(i)//2]
    shalf = i[len(i)//2:]
    for j in fhalf:
        if j in shalf:
            doubles.append(j)
            break


print(f"{doubles=}")
priority = list(string.ascii_lowercase) + list(string.ascii_uppercase)
print(f"{priority=}")


print("\nPriority Numbers:", end=" ")
summe = 0
for i in doubles:
    summe += (priority.index(i) + 1)
    print(priority.index(i)+1, end=" ")


print(f"\n\n{summe=}")


