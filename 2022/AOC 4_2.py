with open('input04.txt') as f:
    lines = f.readlines()

print(lines)

new_list = []
for i in lines:
    formatted = i.replace("-", ",", 2)
    formatted = formatted.replace("\n", "")
    new_list.append(tuple(map(int, formatted.split(','))))

print(new_list)

overlap_count = 0

for i in new_list:
    if i[1] >= i[2] >= i[0] or i[3] >= i[0] >= i[2]:
        overlap_count += 1

print(len(new_list))
print(overlap_count)