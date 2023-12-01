with open('input02.txt') as f:
    lines = f.readlines()

print(lines)

def gamescore(line):
    if (line[0] == 'A' and line[2] == 'Y') or (line[0] == 'B' and line[2] == 'Z') or (line[0] == 'C' and line[2] == 'X'):
        return 6 # Win
    elif (line[0] == 'A' and line[2] == 'Z') or (line[0] == 'B' and line[2] == 'X') or (line[0] == 'C' and line[2] == 'Y'):
        return 0 # Loss
    elif (line[0] == 'A' and line[2] == 'X') or (line[0] == 'B' and line[2] == 'Y') or (line[0] == 'C' and line[2] == 'Z'):
        return 3 # Draw

def signscore(line):
    if (line[0] == 'A' and line[2] == 'X') or (line[0] == 'B' and line[2] == 'Z') or (line[0] == 'C' and line[2] == 'Y'):
        return 3  # Scissors C
    elif (line[0] == 'A' and line[2] == 'Z') or (line[0] == 'B' and line[2] == 'Y') or (line[0] == 'C' and line[2] == 'X'):
        return 2  # Paper B
    elif (line[0] == 'A' and line[2] == 'Y') or (line[0] == 'B' and line[2] == 'X') or (line[0] == 'C' and line[2] == 'Z'):
        return 1  # Rock A


total_score = 0
for i in lines:
    if i[2] == 'X':
        total_score += 0
    if i[2] == 'Y':
        total_score += 3
    if i[2] == 'Z':
        total_score += 6
    total_score += signscore(i)

print(total_score)