from typing import List


def rucksack_duplicate(line: str) -> str:
    n = len(line)
    first, second = set(line[:n // 2]), set(line[n // 2:])
    return (first & second).pop()


def group_duplicate(lines: List[str]) -> str:
    intersection = set(lines[0]) & set(lines[1]) & set(lines[2])
    intersection.remove('\n')
    return intersection.pop()


def get_priority(item: str) -> int:
    if item >= 'a':
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - 38


if __name__ == '__main__':
    with open('../input/03_input.txt', 'r', encoding='utf-8') as f:
        total1 = sum(
            get_priority(rucksack_duplicate(line.strip())) for line in f)
    print(f'Part 1 - Sum of duplicate item priorities: {total1}')
    with open('../input/03_input.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        total2 = 0
        for i in range(0, len(lines), 3):
            total2 += get_priority(group_duplicate(lines[i:i + 3]))
    print(f'Part 2 - Sum of badge priorities: {total2}')
