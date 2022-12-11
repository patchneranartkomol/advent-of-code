from typing import Generator

CHECK_CYCLES = {20, 60, 100, 140, 180, 220}


def check_cycle(cycle: int, strengths: list[int], x: int) -> None:
    if cycle not in CHECK_CYCLES:
        return
    strengths.append(x * cycle)


def draw_pixel(cycle: int, x: int) -> bool:
    pos = (cycle % 40) - 1
    sprite = {x - 1, x, x + 1}
    if pos in sprite:
        return True
    return False


def chunk(_list) -> Generator[list[str], None, None]:
    for i in range(0, len(_list), 40):
        yield _list[i:i + 40]


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

    pixels = []
    with open('../input/10_input.txt', 'r', encoding='utf-8') as f:
        cycle = 0
        x = 1
        for line in f:
            if line.startswith('noop'):
                cycle += 1
                pixels.append('#') if draw_pixel(cycle,
                                                 x) else pixels.append(' ')
            else:
                val = int(line.split(' ')[-1])
                cycle += 1
                pixels.append('#') if draw_pixel(cycle,
                                                 x) else pixels.append(' ')
                cycle += 1
                pixels.append('#') if draw_pixel(cycle,
                                                 x) else pixels.append(' ')
                x += val
    rows = [''.join(r) for r in chunk(pixels)]
    print('Part 2 - CRT displays')
    for r in rows:
        print(r)
