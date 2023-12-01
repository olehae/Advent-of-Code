# Correct Answer for input07.txt: 1315285
# Correct Answer for input07.txt part 2: 9847279
# Correct Answer for input07_fg.txt: 1391690

with open('input07.txt') as f:
    lines = f.readlines()

print(f"{lines=}")

formatted = []
for i in lines:
    formatted.append(i.replace("\n", ""))

formatted = list(filter("$ ls".__ne__, formatted))

print(f"{formatted=}")

commands = []
ls = []

for i in formatted:
    if "$ cd" in i:
        commands.append(i)


def get_values(name, given_value=0):
    index = formatted.index("$ cd "+name)
    count = index+1
    value = given_value
    while True:
        if "dir" in formatted[count]:
            value += get_values(formatted[count][4:])
        elif "$" in formatted[count]:
            break
        else:
            number = int(formatted[count].split(" ")[0])
            value += number
        count += 1
    return value


# dir only list
dir_list1 = [i for i in formatted if i[:3] == "dir"]
print(f"{dir_list1=}")

dir_list2 = []
for i in dir_list1:
    dir_list2.append(i[4:])
dir_list2.append("/")
print(f"{dir_list2=}")

end_summe = 0
for i in dir_list2:
    if get_values(i) < 100000:
        # print(i, "\t", get_values(i))
        end_summe += get_values(i)

print(f"{end_summe=}")
