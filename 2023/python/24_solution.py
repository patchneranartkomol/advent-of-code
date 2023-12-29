from fractions import Fraction
FILENAME = 'input.txt'
BOUNDARIES = (200000000000000, 400000000000000)


class Hailstone:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

        # Standard Form for linear eq: ax + by = c
        self.a = vy
        self.b = -vx
        self.c = vy * x - vx * y


def part_one(hailstones):
    """
    Credit HyperNeutrino for the linear formula conditions
    """
    count = 0
    for i, h1 in enumerate(hailstones):
        for h2 in hailstones[:i]:
            if h1.a * h2.b == h1.b * h2.a:
                continue
            x = (h1.c * h2.b - h2.c * h1.b) / (h1.a * h2.b - h2.a * h1.b)
            y = (h2.c * h1.a - h1.c * h2.a) / (h1.a * h2.b - h2.a * h1.b)
            if not (BOUNDARIES[0] <= x <= BOUNDARIES[1]
                    and BOUNDARIES[0] <= y <= BOUNDARIES[1]):
                continue

            if all(h.vx * (x - h.x) >= 0 and h.vy * (y - h.y) >= 0
                   for h in (h1, h2)):
                count += 1
    return count


def cross_product(h):
    return (h.y * h.vz - h.z * h.vy, h.z * h.vx - h.x * h.vz,
            h.x * h.vy - h.y * h.vx)


def solve_linear_system(linear_system):
    n = len(linear_system)
    coefficients = []
    while linear_system:
        new_coef, linear_system = gaussian_elimination(linear_system)
        coefficients.append(new_coef)
    soln = []
    for var_no in range(n - 1, -1, -1):
        soln.append(sum(coef * sol for coef,
                    sol in zip(coefficients[var_no], soln[::-1] + [1])))
    return soln[::-1]


def gaussian_elimination(linear_system):
    row_to_eliminate = next(row for row in linear_system if row[0] != 0)
    coefficients = [Fraction(-value, row_to_eliminate[0])
                    for value in row_to_eliminate[1:]]
    new_system = []
    for row in linear_system:
        if row != row_to_eliminate:
            new_system.append([value + row[0]*coefficient for value,
                              coefficient in zip(row[1:], coefficients)])
    return coefficients, new_system


def part_two(hailstones):
    """
    Credit janek37 (and other Redditors) for Gaussian elimation approach
    """
    h1, h2, h3 = hailstones[0:3]
    cp1, cp2, cp3 = (cross_product(h) for h in (h1, h2, h3))
    linear_system = [
        [0, h1.vz - h2.vz, h2.vy - h1.vy, 0, h2.z - h1.z, h1.y - h2.y, cp2[0] - cp1[0]],
        [h2.vz - h1.vz, 0, h1.vx - h2.vx, h1.z - h2.z, 0, h2.x - h1.x, cp2[1] - cp1[1]],
        [h1.vy - h2.vy, h2.vx - h1.vx, 0, h2.y - h1.y, h1.x - h2.x, 0, cp2[2] - cp1[2]],
        [0, h1.vz - h3.vz, h3.vy - h1.vy, 0, h3.z - h1.z, h1.y - h3.y, cp3[0] - cp1[0]],
        [h3.vz - h1.vz, 0, h1.vx - h3.vx, h1.z - h3.z, 0, h3.x - h1.x, cp3[1] - cp1[1]],
        [h1.vy - h3.vy, h3.vx - h1.vx, 0, h3.y - h1.y, h1.x - h3.x, 0, cp3[2] - cp1[2]],
    ]
    solution = solve_linear_system(linear_system)
    assert all(sol.denominator == 1 for sol in solution[:3])
    return solution[0] + solution[1] + solution[2]


hailstones = []
with open(FILENAME) as file:
    lines = [line.strip().split('@') for line in file]
    for a, b in lines:
        hailstones.append(
            Hailstone(*(map(int, a.split(','))), *map(int, b.split(','))))

print(f'Part 1 - intersections in test area: {part_one(hailstones)}')
print(f'Part 2 - sum of rock initial coords: {part_two(hailstones)}')
