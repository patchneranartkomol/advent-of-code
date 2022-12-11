CHECK_CYCLES = {20, 60, 100, 140, 180, 220}

def check_cycle(cycle: int, strengths: list[int], x: int) -> None:
    if cycle not in CHECK_CYCLES:
        return
    print(x, cycle)
    strengths.append(x * cycle)

if __name__ == '__main__':
    strengths = []
    with open('../input/10_input.txt', 'r', encoding='utf-8') as f:
        cycle = 0
        x = 1
        for line in f:
            if line.startswith('noop'):
                cycle += 1
                check_cycle(cycle, strengths, x)
            else:
                val = int(line.split(' ')[-1])
                cycle += 1
                check_cycle(cycle, strengths, x)
                cycle += 1
                check_cycle(cycle, strengths, x)
                x += val

    print(f'Part 1: sum of signal strengths: {sum(strengths)}')
