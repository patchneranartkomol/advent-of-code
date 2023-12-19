from heapq import heappush, heappop
FILENAME = 'input.txt'
DIRECTIONS = {(1, 0), (0, 1), (-1, 0), (0, -1)}


def solve(board, min_steps, max_steps):
    queue = []
    seen = set()
    queue.append((0, 0, 0, 0, 0))
    while queue:
        heat, x, y, d_x, d_y = heappop(queue)
        if x == len(board[0]) - 1 and y == len(board) - 1:
            return heat
        if (x, y, d_x, d_y) in seen:
            continue
        seen.add((x, y, d_x, d_y))
        for dx, dy in DIRECTIONS - {(d_x, d_y), (-d_x, -d_y)}:
            i, j, h = x, y, heat
            for k in range(1, max_steps + 1):
                i, j = i + dy, j + dx
                if 0 <= i < len(board[0]) and 0 <= j < len(board):
                    h += int(board[j][i])
                    if k >= min_steps:
                        heappush(queue, (h, i, j, dx, dy))


with open(FILENAME) as file:
    board = [line.strip() for line in file]
print(f'Part 1 - min heat: {solve(board, 1, 3)}')
print(f'Part 2 - min heat: {solve(board, 4, 10)}')
