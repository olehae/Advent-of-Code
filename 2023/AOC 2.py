with open('input02.txt') as f:
    lines = f.read().strip().split("\n")


def part1(lines):
    game_id = 1
    out = 0
    for line in lines:
        line = line.removeprefix(f"Game {game_id}: ")
        rounds = line.split("; ")
        correct = True
        for r in rounds:
            cubes = r.split(", ")
            for cube in cubes:
                cube = cube.split()
                match cube[1]:
                    case "red":
                        amount = 12
                    case "green":
                        amount = 13
                    case "blue":
                        amount = 14
                if int(cube[0]) > amount:
                    correct = False
                    break
            if not correct:
                break
        if correct:
            out += game_id
        game_id += 1

    print(out)


def part2(lines):
    game_id = 1
    out = 0
    for line in lines:
        max_cubes = {}
        line = line.removeprefix(f"Game {game_id}: ")
        rounds = line.split("; ")
        for r in rounds:
            cubes = r.split(", ")
            for cube in cubes:
                cube = cube.split()
                try:
                    if int(cube[0]) > max_cubes[cube[1]]:
                        max_cubes[cube[1]] = int(cube[0])
                except KeyError:
                    max_cubes[cube[1]] = int(cube[0])
        game_power = 1
        for i in max_cubes.values():
            game_power *= i
        out += game_power
        game_id += 1
    print(out)


part2(lines)
