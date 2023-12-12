from copy import deepcopy
from itertools import combinations
FILENAME = 'input.txt'
EXPANSION_FACTOR = 1000000


def visualize_space(space):
    """
    Helper function to visualize space and galaxies
    """
    print('\n')
    for y, row in enumerate(space):
        print(f"{str(y).rjust(3, ' ')}   {''.join(row)}")
    print('\n')


def find_empty_rows(space):
    empty_columns, empty_rows = [], []
    for x in range(len(space[0])):
        if all(val[x] == '.' for val in space):
            empty_columns.append(x)
    for y, row in enumerate(space):
        if all(char == '.' for char in row):
            empty_rows.append(y)
    return empty_columns, empty_rows


def expand_space(space):
    """
    Part 1 helper function
    Expand 2-D list representing space in-place
    """
    empty_columns, empty_rows = find_empty_rows(space)
    for i, x in enumerate(empty_columns):
        for row in space:
            row.insert(x + i, '.')
    for i, y in enumerate(empty_rows):
        space.insert(y + i, ['.' * len(space[0])])


def map_galaxies(space):
    galaxies = {}
    count = 0
    for y, row in enumerate(space):
        for x, char in enumerate(row):
            if char == '#':
                galaxies[count] = (x, y)
                count += 1
    return galaxies


def part_one(space):
    total = 0
    expand_space(space)
    # visualize_space(space)
    galaxies = map_galaxies(space)
    for a, b in combinations(galaxies.keys(), 2):
        x_a, x_b = galaxies[a][0], galaxies[b][0]
        y_a, y_b = galaxies[a][1], galaxies[b][1]
        total += abs(x_a - x_b) + abs(y_a - y_b)
    return total


def part_two(space):
    total = 0
    galaxies = map_galaxies(space)
    empty_columns, empty_rows = find_empty_rows(space)
    for a, b in combinations(galaxies.keys(), 2):
        x_a, x_b = galaxies[a][0], galaxies[b][0]
        y_a, y_b = galaxies[a][1], galaxies[b][1]

        exp_row = exp_col = 0
        for i in range(x_a + 1, x_b):
            if i in empty_columns:
                exp_row += 1
        for i in range(x_a, x_b, -1):
            if i in empty_columns:
                exp_row += 1
        for j in range(y_a + 1, y_b):
            if j in empty_rows:
                exp_col += 1
        for j in range(y_a, y_b, -1):
            if j in empty_rows:
                exp_col += 1

        total += (exp_row + exp_col) * (EXPANSION_FACTOR - 1)
        total += abs(x_a - x_b) + abs(y_a - y_b)
    return total


space = []
with open(FILENAME) as file:
    for line in file:
        space.append([ch for ch in line.strip()])
space_copy = deepcopy(space)
print(f'Part 1: sum of shortest paths: {part_one(space)}')
print(f'Part 2: sum of shortest paths: {part_two(space_copy)}')
