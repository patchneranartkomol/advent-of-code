FILENAME = 'test_input5.txt'

DIRECTIONS = {
    (-1, 0): 'N',
    (1, 0): 'S',
    (0, -1): 'W',
    (0, 1): 'E',
}


def find_start(maze):
    n = len(maze)
    start = None
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 'S':
                start = (i, j)
                break
    if not start:
        raise RuntimeError('Start not found!')
    return start


def start_neighbors(maze, start):
    n = len(maze)
    neighbors = []
    i, j = start
    if 0 <= (i - 1) < n and maze[i - 1][j] in {'|', 'F', '7'}:  # North
        neighbors.append((i - 1, j))
    if 0 <= (i + 1) < n and maze[i + 1][j] in {'|', 'L', 'J'}:  # South
        neighbors.append((i + 1, j))
    if 0 <= (j - 1) < n and maze[i][j - 1] in {'-', 'L', 'F'}:  # West
        neighbors.append((i, j - 1))
    if 0 <= (j + 1) < n and maze[i][j + 1] in {'-', 'J', '7'}:  # East
        neighbors.append((i, j + 1))

    if len(neighbors) != 2:
        raise RuntimeError('Could not determine shape of starting location')
    return neighbors


def part_two(maze):
    n = len(maze)
    count = 0
    return count


def part_one(maze, start):
    # Find valid start directions
    neighbors = start_neighbors(maze, start)

    # Follow the pipe loop in one direction, until we return to the start
    steps = 1
    prev_i, prev_j = start
    i, j = neighbors[0]
    # Track tiles that are part of the main pipe loop
    while (i, j) != start:
        steps += 1
        came_from = DIRECTIONS[prev_i - i, prev_j - j]
        prev_i, prev_j = i, j
        match maze[i][j]:
            case '|':
                if came_from == 'N':
                    i += 1
                else:
                    i -= 1
            case '-':
                if came_from == 'E':
                    j -= 1
                else:
                    j += 1
            case 'L':
                if came_from == 'N':
                    j += 1
                else:
                    i -= 1
            case 'J':
                if came_from == 'N':
                    j -= 1
                else:
                    i -= 1
            case '7':
                if came_from == 'S':
                    j -= 1
                else:
                    i += 1
            case 'F':
                if came_from == 'S':
                    j += 1
                else:
                    i += 1
            case _:
                raise RuntimeError("Unexpected Maze Tile", maze[i][j])

    return steps // 2


maze = []
with open(FILENAME) as file:
    for line in file:
        maze.append(line.strip())
start = find_start(maze)
print(f'Part 1: steps to farthest point: {part_one(maze, start)}')
print(f'Part 2: tiles enclosed by loop {part_two(maze)}')
