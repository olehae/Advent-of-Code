with open('input15.txt') as f:
    lines = f.read().strip().split(",")


def to_hash(string):
    out = 0
    for char in string:
        out += ord(char)
        out *= 17
        out = out % 256
    return out


print(f"Part 1: {sum(to_hash(chars) for chars in lines)}")

hashmap = {i: [] for i in range(256)}
for chars in lines:
    if "=" in chars:
        chars = tuple(chars.split("="))
        box = to_hash(chars[0])
        box_content = hashmap[box]
        try:
            idx = [x[0] for x in box_content].index(chars[0])
            box_content[idx] = chars
        except ValueError:
            box_content.append(chars)
    else:
        chars = chars.replace("-", "")
        box = to_hash(chars)
        box_content = hashmap[box]
        try:
            idx = [x[0] for x in box_content].index(chars)
            del box_content[idx]
        except ValueError:
            pass
    hashmap[box] = box_content

print(f"Part 2: {sum((i + 1) * (j + 1) * int(elem[1]) for i in range(256) for j, elem in enumerate(hashmap[i]))}")
