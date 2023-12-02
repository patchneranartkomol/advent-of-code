FILENAME = 'input.txt'
POSSIBLE_CUBES = {'red': 12, 'green': 13, 'blue': 14}


def check_p1(line):
    rounds = [r.strip() for r in line.split(':')[1].split(';')]
    for r in rounds:
        hands = [h.strip() for h in r.split(',')]
        for h in hands:
            count, color = h.split(' ')
            if int(count) > POSSIBLE_CUBES[color]:
                return False
    return True


def part_one(filename):
    total = 0
    with open(filename) as file:
        for i, line in enumerate(file):
            if check_p1(line):
                total += i + 1
    print(f'Part 1: Sum of IDs: {total}')


def check_p2(line):
    maxes = {'red': 0, 'green': 0, 'blue': 0}
    rounds = [r.strip() for r in line.split(':')[1].split(';')]
    for r in rounds:
        hands = [h.strip() for h in r.split(',')]
        for h in hands:
            count, color = h.split(' ')
            maxes[color] = max(maxes[color], int(count))
    return maxes['red'] * maxes['green'] * maxes['blue']


def part_two(filename):
    total = 0
    with open(filename) as file:
        for line in file:
            total += check_p2(line)
    print(f'Part 2: Sum of Powers: {total}')


part_one(FILENAME)
part_two(FILENAME)
