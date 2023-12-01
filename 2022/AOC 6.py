with open('input06.txt') as f:
    lines = f.readlines()

print(lines)
linestring = lines[0].replace("\n", "")
print(linestring)

temp_list = []
for i in linestring[:4]:
    temp_list.append(i)
packet_start = 4

for i in linestring[4:]:
    if len(temp_list) > len(set(temp_list)):
        temp_list.pop(0)
        temp_list.append(i)
        packet_start += 1

    elif len(temp_list) == len(set(temp_list)):
        break
    print(temp_list)

print(packet_start)
