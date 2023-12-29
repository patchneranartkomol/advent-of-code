from copy import deepcopy
FILENAME = 'input.txt'
DIRECTIONS = {
    '.': [(1, 0), (-1, 0), (0, -1), (0, 1)],
    '^': [(-1, 0)],
    'v': [(1, 0)],
    '<': [(0, -1)],
    '>': [(0, 1)]
}
P2_DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]


def valid_neighbor(grid, y, x):
    return 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] != '#'


def longest_path(graph, start, end):
    seen = set()

    def dfs(vertex):
        if vertex == end:
            return 0
        max_len = -float('inf')
        seen.add(vertex)
        for nv in graph[vertex]:
            if nv not in seen:
                max_len = max(max_len, dfs(nv) + graph[vertex][nv])
        seen.remove(vertex)
        return max_len

    return dfs(start)


def flood_fill(graph, vertices, part):
    for y, x in vertices:
        stack = []
        stack.append((0, y, x))
        seen = set()
        seen.add((y, x))
        while stack:
            n, cy, cx = stack.pop()
            if n != 0 and (cy, cx) in vertices:
                graph[(y, x)][(cy, cx)] = n
                continue
            dirs = DIRECTIONS[grid[cy][cx]] if part == 1 else P2_DIRECTIONS
            for dy, dx in dirs:
                ny, nx = cy + dy, cx + dx
                if valid_neighbor(grid, ny, nx) and (ny, nx) not in seen:
                    stack.append((n + 1, ny, nx))
                    seen.add((ny, nx))


with open(FILENAME) as file:
    grid = [line.strip() for line in file]
start = (0, grid[0].index('.'))
end = (len(grid) - 1, grid[-1].index('.'))
# Edge contraction - translate input grid into vertices of a graph
vertices = [start, end]
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char == '#':
            continue
        neighbors = 0
        for dy, dx in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
            if valid_neighbor(grid, dy, dx):
                neighbors += 1
        if neighbors >= 3:
            vertices.append((y, x))

# Adjacency list representation
graph = {vertex: {} for vertex in vertices}
p2_graph = deepcopy(graph)
flood_fill(graph, vertices, 1)
flood_fill(p2_graph, vertices, 2)

print(f'Part 1 - steps in longest hike {longest_path(graph, start, end)}')
print(f'Part 2 - steps in longest hike {longest_path(p2_graph, start, end)}')
