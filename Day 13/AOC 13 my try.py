with open("input13.txt") as f:
    data = [f.read().strip().split()]

print(f"{data=}")


def compare(left, right):
    right_order = True
    for i, elem in enumerate(left):
        print(elem)
        if type(elem) is int and type(right[i]) is int:
            print(elem)
            if right[i] < elem:
                right_order = False
            elif elem < right[i]:
                right_order = True
                break
        elif type(elem) is list and type(right[i]) is list:
            right_order = compare(elem, right[i])
        elif type(elem) is int and type(right[i]) is list:
            right_order = compare(list(elem), right[i])
        elif type(elem) is list and type(right[i]) is int:
            right_order = compare(elem, list(right[i]))

    return right_order


"""index_count = 0
summe = 0
for i range(0, len(data), 2)):
    index_count += 1
    if compare(elem, data[i + 1]) is True:
        print(index_count)
        summe += index_count

print(f"{summe=}")
"""