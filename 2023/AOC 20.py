from collections import deque
from math import lcm

with open('input20.txt') as f:
    lines = f.read().strip().split("\n")


class Module:
    def __init__(self, name, module_type, send_to):
        self.name = name
        self.send_to = send_to.split(", ")
        match module_type:
            case "%":
                self.mod_type = "flip"
                self.state = False
            case "&":
                self.mod_type = "conjunction"
                self.state = {}


modules = {}
# populate modules dict with name as key and Class as value
for line in lines:
    name, send_to = line.split(" -> ")
    if send_to == "rx":
        # remember the module that triggers rx
        before_rx = name[1:]
    if name == "broadcaster":
        start_modules = send_to.split(", ")
    else:
        module_type = name[0]
        modules[name[1:]] = Module(name[1:], module_type, send_to)

to_rx = {}
for name, module in modules.items():
    # populate conjunction modules with states of the modules they get signal from
    for output in module.send_to:
        if output in modules.keys() and modules[output].mod_type == "conjunction":
            modules[output].state[name] = "low"
        # store the modules that send to the activation module of rx (we know it is a conjunction module)
        if output == before_rx:
            to_rx[module.name] = []

low, high = 0, 0
i = 0
# check if we have found two values for every to_rx element
while any(len(x) < 2 for x in to_rx.values()):
    # we can do Part 1 while searching for Part 2, because Part 2 takes > 1000 steps
    if i == 1000:
        print(f"Part 1: {low * high}")
    i += 1
    low += 1
    # form of item in q is (origin, to, pulse)
    q = deque([("broadcaster", x, "low") for x in start_modules])
    while q:
        origin, to, pulse = q.popleft()
        if pulse == "low":
            low += 1
        else:
            high += 1

        # store button press counts if to_rx modules are activated
        if to == before_rx and pulse == "high":
            to_rx[origin].append(i)

        if to not in modules.keys():
            continue

        module = modules[to]

        if module.mod_type == "flip":
            if pulse == "low":
                module.state = not module.state
                send = "high" if module.state else "low"
                for x in module.send_to:
                    q.append((module.name, x, send))
        # else module type must be conjunction
        else:
            module.state[origin] = pulse
            if all(x == "high" for x in module.state.values()):
                send = "low"
            else:
                send = "high"
            for x in module.send_to:
                q.append((module.name, x, send))

print(f"Part 2: {lcm(*[x[1]-x[0] for x in to_rx.values()])}")
