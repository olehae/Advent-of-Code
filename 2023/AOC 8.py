from math import lcm

with open('input08.txt') as f:
    lines = f.read().strip().split("\n")

instructions = lines[0]

nodes = {}
for line in lines[2:]:
    line = line.replace(")", "").split(" = (")
    nodes[line[0]] = line[1].split(", ")

max_i = len(instructions)


def part1(n):
    node = "AAA"
    count, i = 0, 0
    while node != "ZZZ":
        count += 1
        match instructions[i]:
            case "R":
                node = n[node][1]
            case "L":
                node = n[node][0]
        i += 1
        if i == max_i:
            i = 0
    print(f"Part 1: {count}")


def part2(n):
    current_nodes = [node for node in list(n.keys()) if node.endswith("A")]
    count, i = 0, 0
    shortest_path = {}
    while len(current_nodes) > 0:
        count += 1
        current_nodes = [n[node][1] if instructions[i] == "R" else n[node][0] for node in current_nodes]
        for node in current_nodes:
            if node[-1] == "Z":
                shortest_path[node] = count
                current_nodes.remove(node)
        i += 1
        if i == max_i:
            i = 0
    print(f"{shortest_path = }")
    print(f"Part 2: {lcm(*shortest_path.values())}")


part1(nodes)
part2(nodes)
