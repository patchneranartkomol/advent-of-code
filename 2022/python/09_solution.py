from dataclasses import dataclass

DIRECTIONS = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}
DIAGONALS = {(-1, -1), (-1, 1), (1, 1), (1, -1)}


@dataclass
class Point:
    x: int
    y: int


def follow_point(head: Point, tail: Point) -> Point:
    dx = abs(head.x - tail.x)
    dy = abs(head.y - tail.y)
    if dx + dy == 2:
        if dx == 2:
            tail.x += (head.x - tail.x) // 2
        elif dy == 2:
            tail.y += (head.y - tail.y) // 2
    elif dx + dy >= 3:
        if dx > 1:
            tail.x += (head.x - tail.x) // 2
        else:
            tail.x += head.x - tail.x
        if dy > 1:
            tail.y += (head.y - tail.y) // 2
        else:
            tail.y += head.y - tail.y
    return tail


if __name__ == '__main__':
    head = Point(0, 0)
    tail = Point(0, 0)
    visited = set()
    visited.add((0, 0))
    with open('../input/09_input.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            d, count = line.split(' ')
            count = int(count)

            for i in range(count):
                head.x += DIRECTIONS[d][0]
                head.y += DIRECTIONS[d][1]
                tail = follow_point(head, tail)
                if (tail.x, tail.y) not in visited:
                    visited.add((tail.x, tail.y))

    print(f'Part 1: Tail visited {len(visited)} positions.')

    rope = []
    for _ in range(10):
        rope.append(Point(0, 0))
    visited = set()

    instructions = 0
    with open('../input/09_input.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            d, count = line.split(' ')
            count = int(count)
            for i in range(count):
                rope[0].x += DIRECTIONS[d][0]
                rope[0].y += DIRECTIONS[d][1]

                for i in range(1, 10):
                    rope[i] = follow_point(rope[i - 1], rope[i])

                if (rope[-1].x, rope[-1].y) not in visited:
                    visited.add((rope[-1].x, rope[-1].y))

    print(f'Part 2: Tail visited {len(visited)} positions.')
