import sys
from collections import defaultdict

FILENAME = 'input.txt'
RECURSION_LIMIT = 15_000


def dfs(grid, visited, i, j, direction):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return

    # Avoid infinite loop if we already came from that direction
    if (i, j) in visited:
        if direction in visited[(i, j)]:
            return
    visited[(i, j)].append(direction)

    y, x = direction
    match grid[i][j]:
        case '.':
            dfs(grid, visited, i + y, j + x, direction)
        case '|':
            if y == 0:
                dfs(grid, visited, i + 1, j, (1, 0))
                dfs(grid, visited, i - 1, j, (-1, 0))
            else:
                dfs(grid, visited, i + y, j + x, direction)
        case '-':
            if x == 0:
                dfs(grid, visited, i, j + 1, (0, 1))
                dfs(grid, visited, i, j - 1, (0, -1))
            else:
                dfs(grid, visited, i + y, j + x, direction)
        case '/':
            if x == 1:
                dfs(grid, visited, i - 1, j, (-1, 0))
            elif x == -1:
                dfs(grid, visited, i + 1, j, (1, 0))
            elif y == 1:
                dfs(grid, visited, i, j - 1, (0, -1))
            else:
                dfs(grid, visited, i, j + 1, (0, 1))
        case '\\':
            if x == 1:
                dfs(grid, visited, i + 1, j, (1, 0))
            elif x == -1:
                dfs(grid, visited, i - 1, j, (-1, 0))
            elif y == 1:
                dfs(grid, visited, i, j + 1, (0, 1))
            else:
                dfs(grid, visited, i, j - 1, (0, -1))


def part_one(grid):
    visited = defaultdict(list)
    dfs(grid, visited, 0, 0, (0, 1))
    return len(visited)


def part_two(grid):
    max_score = 0
    # from left
    for i in range(len(grid)):
        visited = defaultdict(list)
        dfs(grid, visited, i, 0, (0, 1))
        max_score = max(max_score, len(visited))
    # from right
    for i in range(len(grid)):
        visited = defaultdict(list)
        dfs(grid, visited, i, len(grid[0]) - 1, (0, -1))
        max_score = max(max_score, len(visited))
    # from bottom
    for i in range(len(grid)):
        visited = defaultdict(list)
        dfs(grid, visited, len(grid) - 1, i, (-1, 0))
        max_score = max(max_score, len(visited))
    # from top
    for i in range(len(grid)):
        visited = defaultdict(list)
        dfs(grid, visited, 0, i, (1, 0))
        max_score = max(max_score, len(visited))
    return max_score


with open(FILENAME) as file:
    grid = [line.strip() for line in file]

# Python's default recursion limit is 1000
# We will can traverse 12000+ tiles with our recursive DFS
sys.setrecursionlimit(RECURSION_LIMIT)
print(f'Part 1 - tiles energized: {part_one(grid)}')
print(f'Part 2 - max tiles energized: {part_two(grid)}')
