with open("input16.txt") as f:
    raw = f.readlines()

data = {}
for i in raw:
    if "; tunnel leads to valve" in i:
        data[i[6:8]] = i[23:].replace("; tunnel leads to valve", "").replace("\n", "").split()
    else:
        data[i[6:8]] = i[23:].replace("; tunnels lead to valves", "").replace("\n", "").split()
    data[i[6:8]][0] = int(data[i[6:8]][0])


for i in data:
    print(f"{i}: {data[i]}")

