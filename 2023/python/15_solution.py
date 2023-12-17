from collections import defaultdict
FILENAME = 'input.txt'


def _hash(sequence):
    curr = 0
    for char in sequence:
        curr += ord(char)
        curr *= 17
        curr %= 256
    return curr


def part_one(line):
    return sum(_hash(seq) for seq in line.split(','))


def search_box(box, label):
    for i, pair in enumerate(box):
        if pair[0] == label:
            return i
    return -1


def score(boxes):
    return sum(
        sum((box_num + 1) * (i + 1) * lens[-1] for i, lens in enumerate(slots))
        for box_num, slots in boxes.items())


def part_two(line):
    boxes = defaultdict(list)
    for seq in line.split(','):
        if seq[-1] == '-':
            label = seq.split('-')[0]
            box_num = _hash(label)
            i = search_box(boxes[box_num], label)
            if i != -1:
                del boxes[box_num][i]
        else:
            label, lens = seq.split('=')
            lens = int(lens)
            box_num = _hash(label)
            i = search_box(boxes[box_num], label)
            if i != -1:
                boxes[box_num][i] = (label, lens)
            else:
                boxes[box_num].append((label, lens))
    return score(boxes)


with open(FILENAME) as file:
    line = file.readline().strip()

print(f'Part 1 - sum of HASHes: {part_one(line)}')
print(f'Part 2 - focusing power: {part_two(line)}')
