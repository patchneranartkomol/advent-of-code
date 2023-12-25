from collections import deque
FILENAME = 'input.txt'
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
GRID_STEPS = [65, 196, 327]
P2_STEP_GOAL = 26501365


def expand_grid(grid, factor):
    return [
        [
            grid[i % len(grid)][j % len(grid[0])]
            for j in range(factor * len(grid[0]))
        ]
        for i in range(factor * len(grid))
    ]


def bfs(grid, start, steps):
    m, n = len(grid), len(grid[0])
    queue = deque()
    reached, visited = set(), set()
    queue.append(start)
    while queue:
        i, j, steps = queue.popleft()
        if (i, j) in visited:
            continue
        visited.add((i, j))
        if steps % 2 == 0:
            reached.add((i, j))
        for dx, dy in DIRECTIONS:
            x, y = i + dx, j + dy
            if (0 <= x < m and 0 <= y < n and grid[x][y] != '#'
                    and steps > 0):
                queue.append((x, y, steps - 1))
    return len(reached)


def part_one(grid, steps):
    m, n = len(grid), len(grid[0])
    start = None
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'S':
                start = (i, j, steps)
    return bfs(grid, start, steps)


def part_two(grid, steps):
    expanded = expand_grid(grid, 7)
    a = []
    for stepcount in GRID_STEPS:
        start = len(expanded) // 2, len(expanded[0]) // 2
        a.append((bfs(expanded, (*start, stepcount), stepcount)))

    # Interpolate entire grid with Lagrange polynomial.
    b0 = a[0]
    b1 = a[1] - a[0]
    b2 = a[2] - a[1]
    n = steps // len(grid)
    return b0 + b1 * n + (n * (n - 1) // 2) * (b2 - b1)


with open(FILENAME) as file:
    grid = [line.strip() for line in file]

print(f'Part 1 - # of garden plots: {part_one(grid, 64)}')
print(f'Part 2 - # of garden plots: {part_two(grid, P2_STEP_GOAL)}')
