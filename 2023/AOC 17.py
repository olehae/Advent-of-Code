from heapq import heappop, heappush

with open('input17.txt') as f:
    lines = f.read().strip().split("\n")


def modified_dijkstra(grid, min_straight, max_straight):
    m, n = len(grid), len(grid[0])
    seen = set()
    priority_queue = [(0, 0, 0, 0, 0, 0)]

    while priority_queue:
        # heap is sorted by first element -> heappop always gets lowest score available
        score, i, j, dir_i, dir_j, straight = heappop(priority_queue)

        # Current pos is bottom right and crucible can stop
        if (i, j) == (m-1, n-1) and straight >= min_straight:
            return score

        if (i, j, dir_i, dir_j, straight) in seen:
            continue
        seen.add((i, j, dir_i, dir_j, straight))

        # Move in same direction
        if straight < max_straight and (dir_i, dir_j) != (0, 0):
            next_i = i+dir_i
            next_j = j+dir_j
            if 0 <= next_i < m and 0 <= next_j < n:
                new_score = grid[next_i][next_j] + score
                heappush(priority_queue, (new_score, next_i, next_j, dir_i, dir_j, straight+1))

        # Move in different direction (turn)
        if straight >= min_straight or (dir_i, dir_j) == (0, 0):
            for next_dir_i, next_dir_j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                # Only left / right turns are valid
                if (next_dir_i, next_dir_j) != (dir_i, dir_j) and (next_dir_i, next_dir_j) != (-dir_i, -dir_j):
                    next_i = i + next_dir_i
                    next_j = j + next_dir_j
                    if 0 <= next_i < m and 0 <= next_j < n:
                        new_score = grid[next_i][next_j] + score
                        heappush(priority_queue, (new_score, next_i, next_j, next_dir_i, next_dir_j, 1))


grid = [list(map(int, x)) for x in lines]
print(f"Part 1: {modified_dijkstra(grid, 0, 3)}")
print(f"Part 2: {modified_dijkstra(grid, 4, 10)}")
