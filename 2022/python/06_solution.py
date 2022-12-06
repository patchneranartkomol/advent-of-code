def find_unique(marker_size: int, line: str, start: int=0) -> int:
    for i in range(start + marker_size, len(line)):
        if len(set(line[i - marker_size:i])) == marker_size:
            return i
    return -1


if __name__ == '__main__':
    with open('../input/06_input.txt', 'r', encoding='utf-8') as f:
        line = f.readline().strip()

    start =find_unique(4, line)
    print(f'Part 1 - start-of-packet marker: {start}')
    print(f'Part 2 - start-of-message marker: {find_unique(14, line, start)}')
