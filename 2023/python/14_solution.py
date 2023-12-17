FILENAME = 'input.txt'
CYCLES = 1_000_000_000


def tilt(platform):
    new_platform = []
    for col in platform:
        tilted = []
        for group in col.split('#'):
            tilted.append(
                ''.join(['O'] * group.count('O') + ['.'] * group.count('.')))
        new_platform.append('#'.join(tilted))
    return new_platform


def transpose(platform):
    return [''.join(r) for r in zip(*platform)]


def rotate(platform):
    """
    Rotates the platform clockwise.

    Credit: /u/CrAzYmEtAlHeAd1 and u/errop_
    """
    return [''.join(line) for line in zip(*map(reversed, platform))]


def cycle(platform):
    for _ in range(4):
        platform = rotate(tilt(platform))
    return platform


def score(platform):
    return sum(
        sum((i * (char == 'O')) for i, char in enumerate(col[::-1], 1))
        for col in platform)


def part_one(platform):
    return score(tilt(platform))


def part_two(platform):
    visited = []
    while platform not in visited:
        visited.append(platform)
        platform = cycle(platform)

    # Once a loop has been found, identify and score platform at that point
    loop_start = visited.index(platform)
    loop_len = len(visited) - loop_start
    final_position = (CYCLES - loop_start) % loop_len + loop_start
    return score(visited[final_position])


with open(FILENAME) as file:
    lines = [line.strip() for line in file]
# Work with a columnar representation of the platform
platform = transpose(lines)
print(f'Part 1 - total load: {part_one(platform)}')
print(f'Part 1 - total load: {part_two(platform)}')
