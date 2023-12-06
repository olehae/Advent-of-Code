from sympy import Symbol, Eq, solve
import math

with open('input06.txt') as f:
    lines = f.read().strip().split("\n")


def part1(lines):
    time_distance = list(zip(*[list(map(int, line.split()[1:])) for line in lines]))

    out = 1
    for time, distance in time_distance:
        wins = 0
        for i in range(time):
            pot_distance = i * (time-i)
            if pot_distance > distance:
                wins += 1
        out *= wins
    print(f"Part 1: {out}")


def part2(lines):
    time, distance = [int("".join(line.split()[1:])) for line in lines]
    x = Symbol("x")
    equation = Eq(x*(time-x), distance)
    solved = solve(equation, x)
    solved = [s.evalf() for s in solved]
    possible_ways = math.ceil(solved[1]) - math.ceil(solved[0])
    print(f"Part 2: {possible_ways}")


part1(lines)
part2(lines)
