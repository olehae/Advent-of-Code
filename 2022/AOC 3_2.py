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

"""print(formatted[0][:len(formatted[0])//2])
print(formatted[0][len(formatted[0])//2:])"""

badge = []
for i in formatted[::3]:
    ind = formatted.index(i)
    for j in i:
        if j in formatted[(ind+1)] and j in formatted[(ind+2)]:
            badge.append(j)
            break


print(f"{badge=}")
priority = list(string.ascii_lowercase) + list(string.ascii_uppercase)
print(f"{priority=}")


print("\nPriority Numbers:", end=" ")
summe = 0
for i in badge:
    summe += (priority.index(i) + 1)
    print(priority.index(i)+1, end=" ")


print(f"\n\n{summe=}")

print(len(lines))
print(len(formatted))
print(len(badge))