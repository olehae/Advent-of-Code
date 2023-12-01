with open('input01.txt') as f:
    lines = f.read().strip().split("\n")


def part1(lines):
    result = 0
    for line in lines:
        num = list(filter(str.isnumeric, line))
        result += int(num[0]+num[-1])

    print(result)


def part2(lines):
    result = 0
    nums = {"one": "one1one",
            "two": "two2two",
            "three": "three3three",
            "four": "four4four",
            "five": "five5five",
            "six": "six6six",
            "seven": "seven7seven",
            "eight": "eight8eight",
            "nine": "nine9nine"
            }
    for line in lines:
        for key in nums.keys():
            line = line.replace(key, nums[key])
        num = list(filter(str.isnumeric, line))
        result += int(num[0] + num[-1])

    print(result)


part1(lines)
part2(lines)
