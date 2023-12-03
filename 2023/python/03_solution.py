FILENAME = 'input.txt'


# Part 1 - Helper Functions
def visit_number(i, j, n, lines, visited):
    visited.add((i, j))
    # Read to the right until end of number
    x = j
    while x < n:
        if lines[i][x].isdigit():
            visited.add((i, x))
        else:
            break
        x += 1

    # Check neighbors for non-'.' symbol
    neighbor_coords = ((a, b) for a in range(i - 1, i + 2)
                       for b in range(j - 1, x + 1)
                       if (0 <= a < n and 0 <= b < n))
    if any((lines[a][b] != '.' and not lines[a][b].isdigit()
            for a, b in neighbor_coords)):
        return int(lines[i][j:x])
    return 0


def part_one(lines):
    total = 0
    visited = set()
    n = len(lines[0])  # Input is assumed to be square.

    for i in range(n):
        for j in range(n):
            if (i, j) in visited or lines[i][j] == '.':
                continue
            if lines[i][j].isdigit():
                total += visit_number(i, j, n, lines, visited)

    print(f'Part 1: Sum of part numbers: {total}')


# Part 2 - Helpers
class PartNumber:
    def __init__(self, value, coords):
        self.value = value
        self.coords = coords


def create_number(i, j, n, lines, visited):
    visited.add((i, j))
    x = j
    while x < n:
        if lines[i][x].isdigit():
            visited.add((i, x))
        else:
            break
        x += 1

    # Check neighbors for non-'.' symbol
    neighbor_coords = ((a, b) for a in range(i - 1, i + 2)
                       for b in range(j - 1, x + 1)
                       if (0 <= a < n and 0 <= b < n))
    if any((lines[a][b] != '.' and not lines[a][b].isdigit()
            for a, b in neighbor_coords)):
        return PartNumber(int(lines[i][j:x]), set((i, k)
                                                  for k in range(j, x)))
    return None


def gear_ratio(i, j, lines, part_numbers):
    n = len(lines[0])
    neighbor_parts = set()
    neighbor_coords = [(a, b) for a in range(i - 1, i + 2)
                       for b in range(j - 1, j + 2)
                       if (0 <= a < n and 0 <= b < n)]
    for coords in neighbor_coords:
        for part in part_numbers:
            if coords in part.coords:
                neighbor_parts.add(part)
    if len(neighbor_parts) == 2:
        first, second = neighbor_parts.pop(), neighbor_parts.pop()
        return first.value * second.value
    return 0


def part_two(lines):
    n = len(lines[0])

    # Record all part numbers
    visited, part_numbers = set(), []
    for i in range(n):
        for j in range(n):
            if (i, j) in visited or lines[i][j] == '.':
                continue
            if lines[i][j].isdigit():
                p = create_number(i, j, n, lines, visited)
                if p:
                    part_numbers.append(p)

    # Check each '*' adjacent to 2 part numbers
    total = 0
    for i in range(n):
        for j in range(n):
            if lines[i][j] == '*':
                total += gear_ratio(i, j, lines, part_numbers)

    print(f'Part 2: Sum of gear ratios: {total}')


with open(FILENAME) as file:
    lines = [line.strip() for line in file]
part_one(lines)
part_two(lines)
