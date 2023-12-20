import sys
FILENAME = 'input.txt'
GRID_SIZE = 1000
START = (500, 500)
RECURSION_LIMIT = 25_000

DIRECTIONS = {'R': (1, 0),
              'D': (0, 1),
              'L': (-1, 0),
              'U': (0, -1)}
DIR_MAP = {'0': (1, 0),
           '1': (0, 1),
           '2': (-1, 0),
           '3': (0, -1)}


def dfs_fill(grid, x, y):
    if grid[y][x] == '#':
        return
    grid[y][x] = '#'
    for dx, dy in DIRECTIONS.values():
        dfs_fill(grid, x + dx, y + dy)


def part_one(grid, dig_plan):
    """
    Draw out the grid and use DFS to Flood Fill
    """
    x, y = START
    grid[y][x] = '#'
    for dr, meters, _ in dig_plan:
        for _ in range(meters):
            x += DIRECTIONS[dr][1]
            y += DIRECTIONS[dr][0]
            grid[y][x] = '#'
    dfs_fill(grid, START[0] + 1, START[1] + 1)
    return sum(r.count('#') for r in grid)


def part_two(dig_plan):
    """
    Apply Shoelace formula and Pick's Theorem
    """
    x = y = perimeter = 0
    points = []
    for _, _, color in dig_plan:
        direction, count = DIR_MAP[color[6]], int(color[1:6], 16)
        dx, dy = direction
        perimeter += count
        points.append((x, y))
        x += dx * count
        y += dy * count

    area = 0
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        area += x1 * y2 - x2 * y1
    area = abs(area) // 2

    # Credit - mbottini
    # A - ( b / 2 ) + 1 + b => A + b / 2 + 1
    return area + perimeter // 2 + 1


dig_plan = []
with open(FILENAME) as file:
    for line in file:
        dr, meters, color = line.strip().split(' ')
        dig_plan.append((dr, int(meters), color.strip('()')))
grid = [['.'] * GRID_SIZE for _ in range(GRID_SIZE)]


sys.setrecursionlimit(RECURSION_LIMIT)
print(f'Part 1 - cubic meters of lava: {part_one(grid, dig_plan)}')
print(f'Part 2 - cubic meters of lava: {part_two(dig_plan)}')
