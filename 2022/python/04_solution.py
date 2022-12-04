def fully_contains(a_start: int, a_end: int, b_start: int, b_end: int) -> bool:
    if a_start >= b_start and a_end <= b_end:
        return True
    elif b_start >= a_start and b_end <= a_end:
        return True
    return False


def overlaps(a_start: int, a_end: int, b_start: int, b_end: int) -> bool:
    if a_end < b_start or b_end < a_start:
        return False
    return True


if __name__ == '__main__':
    with open('../input/04_input.txt', 'r', encoding='utf-8') as f:
        total1 = 0
        for line in f:
            a, b = line.strip().split(',')
            a_start, a_end = map(int, a.split('-'))
            b_start, b_end = map(int, b.split('-'))
            total1 += fully_contains(a_start, a_end, b_start, b_end)
    print(f'Part 1 - Fully contained assignment pairs: {total1}')

    with open('../input/04_input.txt', 'r', encoding='utf-8') as f:
        total2 = 0
        for line in f:
            a, b = line.strip().split(',')
            a_start, a_end = map(int, a.split('-'))
            b_start, b_end = map(int, b.split('-'))
            total2 += overlaps(a_start, a_end, b_start, b_end)
    print(f'Part 2 - Overlapping assignment pairs: {total2}')
