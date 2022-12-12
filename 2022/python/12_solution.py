from collections import deque

DIRECTIONS = {
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
}


def find_start_end(lines: list[list[str]]) -> tuple[tuple[int, int], tuple[int, int]]:
    start = tuple()
    end = tuple()
    n, m = len(lines), len(lines[0])
    for i in range(n):
        for j in range(m):
            if lines[i][j] == 'S':
                start = (i, j)
                lines[i][j] = 'a'
            elif lines[i][j] == 'E':
                end = (i, j)
                lines[i][j] = 'z'
    return start, end


def bfs_shortest_path(lines: list[list[str]]) -> tuple[int, tuple[int, int]]:
    n, m = len(lines), len(lines[0])
    queue = deque()
    start, end = find_start_end(lines)
    queue.append(start)
    counts = {}
    counts[start] = 0

    while queue:
        i, j = queue.popleft()
        if (i, j) == end:
            return counts[end], end
        for nx, ny in ((i + x, j + y) for x, y in DIRECTIONS):
            if (0 <= nx < n and 0 <= ny < m and (nx, ny) not in counts and
                ord(lines[nx][ny]) - ord(lines[i][j]) <= 1):
                queue.append((nx, ny))
                counts[(nx, ny)] = counts[(i, j)] + 1
    raise RuntimeError('E not found')


def bfs_all_a_shortest_path(lines: list[list[str]], end: tuple[int, int]) -> int:
    n, m = len(lines), len(lines[0])
    queue = deque()
    counts = {}

    for i in range(n):
        for j in range(m):
            if lines[i][j] == 'a':
                queue.append((i, j))
                counts[(i, j)] = 0


    while queue:
        i, j = queue.popleft()
        if (i, j) == end:
            return counts[end]
        for nx, ny in ((i + x, j + y) for x, y in DIRECTIONS):
            if (0 <= nx < n and 0 <= ny < m and (nx, ny) not in counts and
                ord(lines[nx][ny]) - ord(lines[i][j]) <= 1):
                queue.append((nx, ny))
                counts[(nx, ny)] = counts[(i, j)] + 1
    raise RuntimeError('E not found')


with open('../input/12_input.txt', 'r', encoding='utf-8') as f:
    lines = [list(line.strip('\n')) for line in f.readlines()]

p1, end = bfs_shortest_path(lines)
print(f'Part 1: Shortest Path length: {p1}')
print(f'Part 2: Shortest Path length from any a: {bfs_all_a_shortest_path(lines, end)}')
