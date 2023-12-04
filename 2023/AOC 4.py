with open('input04.txt') as f:
    lines = f.read().strip().split("\n")


def val_to_out(val):
    if val == 0:
        return 0
    if val == 1:
        return 1
    else:
        return 2 ** (val-1)


processed = [line.split(": ") for line in lines]
processed = [(first.split()[1], second.split(" | ")) for first, second in processed]


def part1(processed):
    out = 0
    for p in processed:
        winning, nums = p[1]
        # winning = list(map(int, winning.split()))
        winning = winning.split()
        nums = nums.split()

        out += val_to_out(sum(nums.count(i) for i in winning))
    print(f"Part 1: {out}")


def part2(processed):
    card_amount = {int(p[0]): 1 for p in processed}
    for p in processed:
        current = int(p[0])
        winning, nums = p[1]
        winning = winning.split()
        nums = nums.split()
        wins = sum(nums.count(i) for i in winning)
        for i in range(1, wins+1):
            card_amount[current+i] += card_amount[current]

    print(f"Part 2: {sum(card_amount.values())}")


part1(processed)
part2(processed)
