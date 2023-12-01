with open('input04_fg.txt') as f:
    lines = f.readlines()

print(lines)

new_list = []
for i in lines:
    first_elf = ""
    second_elf = ""
    comma = False
    for j in i:
        if j == ",":
            comma = True
        if not comma:
            first_elf += j
        elif comma and j != "\n":
            second_elf += j
    second_elf = second_elf.replace(",", "")
    first_elf = first_elf.replace("-", ",")
    first_elf = first_elf + ","
    second_elf = second_elf.replace("-", ",")
    new_list.append(tuple(map(int, (first_elf+second_elf).split(','))))

print(new_list)

contain_count = 0
for i in new_list:
    if i[0] >= i[2] and i[1] <= i[3]:
        contain_count += 1
    elif i[0] <= i[2] and i[1] >= i[3]:
        contain_count += 1

print(len(new_list))
print(contain_count)