from math import prod

with open('input19.txt') as f:
    workflows, parts = f.read().strip().split("\n\n")

workflows = {x.split("{")[0]: x.split("{")[1][:-1].split(",") for x in workflows.split("\n")}
parts = [{x.split("=")[0]: x.split("=")[1] for x in part[1:-1].split(",")} for part in parts.split("\n")]

out = 0
for part in parts:
    cur_w = "in"
    while cur_w not in ["A", "R"]:
        for comp in workflows[cur_w]:
            if comp == workflows[cur_w][-1]:
                cur_w = comp
            else:
                check, res = comp.split(":")
                check = check.replace(check[0], part[check[0]])
                if eval(check):
                    # End inner for loop and go to next workflow
                    cur_w = res
                    break

    if cur_w == "A":
        out += sum(list(map(int, part.values())))

print(f"Part 1: {out}")


def part2(num_ranges, workflow="in"):
    if workflow == "R":
        return 0
    if workflow == "A":
        # + 1 because range is inclusive, prod gives all combination possibilities
        return prod(x[1] - x[0] + 1 for x in num_ranges.values())

    # iterate over one specific workflow
    workflow = workflows[workflow]
    total = 0
    # [:-1] because the last item is the else statement
    for rule in workflow[:-1]:
        eq, next_wf = rule.split(":")
        char, sign, num = eq[0], eq[1], int(eq[2:])
        lower, upper = num_ranges[char]
        if sign == "<":
            correct = (lower, num-1)
            incorrect = (num, upper)
        else:
            correct = (num+1, upper)
            incorrect = (lower, num)

        if correct[0] <= correct[1]:
            new_ranges = num_ranges.copy()
            new_ranges[char] = correct
            # Recursion with the part of the range that satisfies the equation
            total += part2(new_ranges, workflow=next_wf)
        if incorrect[0] <= incorrect[1]:
            # continue to next statement with range that hasn't satisfied an equation yet
            num_ranges = num_ranges.copy()
            num_ranges[char] = incorrect
        else:
            # This triggers if the incorrect range is empty
            break
    # This triggers if the break above is not used -> if there is still range that hasn't satisfied any equation
    else:
        # workflow[-1] is the else case of the workflow
        total += part2(num_ranges, workflow=workflow[-1])

    return total


print(f"Part 2: {part2({x: (1, 4000) for x in ['x', 'm', 'a', 's']}, workflow='in')}")
