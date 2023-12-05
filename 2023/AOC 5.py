with open('input05.txt') as f:
    lines = f.read().strip().split("\n")

part1_seeds = list(map(int, lines[0].removeprefix("seeds: ").split()))
part2_seeds = [(part1_seeds[i], part1_seeds[i]+part1_seeds[i+1]) for i in range(0, len(part1_seeds), 2)]

# create almanac from text
new = False
current = []
almanac = []
for line in lines[1:]:
    if new:
        new = False
        continue
    if line == "":
        if current:
            almanac.append(current)
            current = []
        new = True
        continue
    current.append(tuple(map(int, line.split())))
if current:
    almanac.append(current)


def transform_seed(seed):
    for transformation in almanac:
        for dest_s, source_s, range_l in transformation:
            if source_s <= seed < source_s + range_l:
                seed = dest_s + (seed - source_s)
                break

    return seed


def transform_ranges(seeds):
    for transformation in almanac:
        new = []
        while len(seeds) > 0:
            start, end = seeds.pop()
            for dest_s, source_s, range_l in transformation:
                overlap_start = max(start, source_s)
                overlap_end = min(end, source_s+range_l)
                if overlap_start < overlap_end:
                    new.append((overlap_start - source_s + dest_s, overlap_end - source_s + dest_s))
                    if overlap_end < end:
                        seeds.append((overlap_end, end))
                    if overlap_start > start:
                        seeds.append((start, overlap_start))
                    break
            else:
                new.append((start, end))
        seeds = new
    return seeds


print(f"Part 1: {min(transform_seed(seed) for seed in part1_seeds)}")

print(f"Part 2: {min(transform_ranges(part2_seeds), key=lambda x: x[0])[0]}")
