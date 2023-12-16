FILENAME = 'input.txt'


def horizontal_reflection(p):
    for i in range(1, len(p)):
        if all(left == right for left, right in zip(reversed(p[:i]), p[i:])):
            return i
    return 0


def vertical_reflection(p):
    return horizontal_reflection(list(zip(*p)))


def part_one(patterns):
    total = 0
    for p in patterns:
        if h := horizontal_reflection(p):
            total += h * 100
        else:
            total += vertical_reflection(p)
    return total


def diff(left, right):
    return sum(a != b for a, b in zip(left, right))


def horizontal_smudged_reflection(p):
    for i in range(1, len(p)):
        # Credit: https://advent-of-code.xavd.id/
        if (sum(diff(left, right)
                for left, right in zip(reversed(p[:i]), p[i:])) == 1):
            return i
    return 0


def vertical_smudged_reflection(p):
    return horizontal_smudged_reflection(list(zip(*p)))


def part_two(patterns):
    total = 0
    for p in patterns:
        if h := horizontal_smudged_reflection(p):
            total += h * 100
        else:
            total += vertical_smudged_reflection(p)
    return total


patterns, lines = [], []
with open(FILENAME) as file:
    for line in file:
        if line == '\n':
            patterns.append(lines)
            lines = []
        else:
            lines.append(line.strip())
patterns.append(lines)
print(f'Part 1: sum of notes: {part_one(patterns)}')
print(f'Part 2: sum of notes: {part_two(patterns)}')
