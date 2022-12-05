def load_stacks_from_input(stacks, lines):
    for i in range(7, -1, -1):
        for j in range(1, len(lines[i]), 4):
            idx = j // 4 + 1
            if lines[i][j] != ' ':
                stacks[idx].append(lines[i][j])


if __name__ == '__main__':
    with open('../input/05_input.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    stacks = [[] for _ in range(10)]
    load_stacks_from_input(stacks, lines)
    assert stacks[1] == ['Q', 'W', 'P', 'S', 'Z', 'R', 'H', 'D']
    assert stacks[9] == ['W', 'P', 'V', 'M', 'B', 'H']

    for instructions in lines[10:]:
        tokens = instructions.strip().split(' ')
        count, source, target = map(int, (tokens[1], tokens[3], tokens[5]))
        for _ in range(count):
            crate = stacks[source].pop()
            stacks[target].append(crate)

    tops = ''.join(stacks[i][-1] for i in range(1, 10))
    print(f'Part 1 - Tops of each stack: {tops}')

    stacks = [[] for _ in range(10)]
    load_stacks_from_input(stacks, lines)

    for instructions in lines[10:]:
        tokens = instructions.strip().split(' ')
        count, source, target = map(int, (tokens[1], tokens[3], tokens[5]))
        stacks[target] += stacks[source][-count:]
        del stacks[source][-count:]

    tops = ''.join(stacks[i][-1] for i in range(1, 10))
    print(f'Part 2 - Tops of each stack: {tops}')
