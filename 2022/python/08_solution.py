from functools import reduce


def scenic_score(grid: list[list[int]], i: int, j: int) -> bool:
    n = len(grid)
    height = grid[i][j]

    scores = []

    treelines = [
            grid[i][:j][::-1],
            grid[i][j + 1 :],
            [r[j] for r in grid[:i]][::-1],
            [r[j] for r in grid[i + 1 :]],
    ]
    for line in treelines:
        for dist, h in enumerate(line, 1):
            if h >= height:
                scores.append(dist)
                break
        else:
            scores.append(max(1, len(line)))
    # Check each direction, stop if you reach an edge or at the first tree 
    # that is the same height or taller than the tree under consideration

    return reduce(lambda a, b: a * b, scores)

def check_visible(grid: list[list[int]], i: int, j: int) -> bool:
    n = len(grid)
    if i == 0 or j == 0 or i == n - 1 or j == n - 1:
        return True
    height = grid[i][j]
    # Check each direction
    if all(grid[i][y] < height for y in range(j)):
        return True
    if all(grid[i][y] < height for y in range(j + 1, n)):
        return True
    if all(grid[x][j] < height for x in range(i)):
        return True
    if all(grid[x][j] < height for x in range(i + 1, n)):
        return True
    return False


if __name__ == '__main__':
    grid = [] # Store n x n input as List[List[int]]
    with open('../input/08_input.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            grid.append([int(c) for c in line.strip()])
    n = len(grid)

    total = 0
    for i in range(n):
        for j in range(n):
            val = check_visible(grid, i, j)
            total += val
    print(f'Part 1: Trees visible: {total}')

    max_score = 0
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            score = scenic_score(grid, i, j)
            max_score = max(score, max_score)
    print(f'Part 2: Max scenic score {max_score}')
