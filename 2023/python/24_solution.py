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

    def __repr__(self):
        return f'Hailstone: a: {self.a}, b: {self.b}, c: {self.c}'


def part_one(hailstones):
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


hailstones = []
with open(FILENAME) as file:
    lines = [line.strip().split('@') for line in file]
    for a, b in lines:
        hailstones.append(
            Hailstone(*(map(int, a.split(','))), *map(int, b.split(','))))

print(f'Part 1 - intersections in test area: {part_one(hailstones)}')
