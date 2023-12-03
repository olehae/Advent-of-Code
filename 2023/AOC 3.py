with open('input03.txt') as f:
    lines = f.read().strip().split("\n")

splitlines = [list(line) for line in lines]


def check_for_symbol(x, y, grid):
    x_max = len(grid[0])
    y_max = len(grid)

    around = [(x+1, y-1), (x+1, y), (x+1, y+1), (x, y-1), (x, y+1), (x-1, y-1), (x-1, y), (x-1, y+1)]

    for i, (x, y) in enumerate(around):
        if 0 <= x < x_max and 0 <= y < y_max:
            element = grid[y][x]
            if not element.isnumeric() and element != ".":
                return True
    return False


def check_for_gear(x, y, grid):
    x_max = len(grid[0])
    y_max = len(grid)

    around = [(x+1, y-1), (x+1, y), (x+1, y+1), (x, y-1), (x, y+1), (x-1, y-1), (x-1, y), (x-1, y+1)]

    for i, (x, y) in enumerate(around):
        if 0 <= x < x_max and 0 <= y < y_max:
            element = grid[y][x]
            if not element.isnumeric() and element == "*":
                return True, (x, y)
    return False, None


def part1(splitlines):
    out = 0
    current_num = ""
    flag = False
    for i, line in enumerate(splitlines):

        # if last elem of line is valid num
        if flag and len(current_num) > 0:
            out += int(current_num)

        # Reset variables for new line
        current_num = ""
        flag = False

        for j, elem in enumerate(line):
            if elem.isnumeric():
                current_num += elem
                if not flag:
                    flag = check_for_symbol(j, i, splitlines)
            # valid word complete
            elif flag and len(current_num) > 0:
                out += int(current_num)
                current_num = ""
                flag = False
            # invalid word complete
            else:
                current_num = ""
                flag = False

    # if very last elem is valid num
    if flag and len(current_num) > 0:
        out += int(current_num)

    print(f"Part 1: {out}")


def part2(splitlines):
    current_num = ""
    gears = {}
    flag = False
    key = None
    for i, line in enumerate(splitlines):

        # if last elem of line is valid num
        if flag and len(current_num) > 0:
            try:
                gears[key].append(int(current_num))
            except KeyError:
                gears[key] = [int(current_num)]

        # Reset variables for new line
        current_num = ""
        flag = False

        for j, elem in enumerate(line):
            if elem.isnumeric():
                current_num += elem
                if not flag:
                    flag, key = check_for_gear(j, i, splitlines)
            # valid word complete
            elif flag and len(current_num) > 0:
                try:
                    gears[key].append(int(current_num))
                except KeyError:
                    gears[key] = [int(current_num)]
                current_num = ""
                flag = False
            # invalid word complete
            else:
                current_num = ""
                flag = False

    # if very last elem is valid num
    if flag and len(current_num) > 0:
        print(current_num)
        try:
            gears[key].append(int(current_num))
        except KeyError:
            gears[key] = [int(current_num)]

    print(f"Part 2: {sum(x[0]*x[1] for x in gears.values() if len(x) == 2)}")


part1(splitlines)
part2(splitlines)
