from collections import deque
from heapq import heapify, heappop
FILENAME = 'input.txt'
FLOOR_LEVEL = 1


class Brick:
    def __init__(self, coords):
        self.start, self.end = coords[0], coords[1]
        self.floor = min(self.start[-1], self.end[-1])
        self.height = abs(self.start[-1] - self.end[-1])
        self.supports = []
        self.supporting = []

    def __lt__(self, other):
        return self.floor < other.floor

    def safely_disintegrate(self):
        return (sum(1 for s in self.supporting if len(s.supports) > 1)
                == len(self.supporting))

    def would_fall(self):
        fallen = set()
        fall_queue = deque((br for br in self.supporting
                            if len(br.supports) == 1))
        while fall_queue:
            falling_brick = fall_queue.popleft()
            fallen.add(falling_brick)
            fall_queue.extend(br for br in falling_brick.supporting
                              if not set(br.supports).difference(fallen))
        return len(fallen)


def drop(bricks):
    heapify(bricks)
    stable_bricks = []
    while bricks:
        brick = heappop(bricks)

        if brick.floor != FLOOR_LEVEL:
            supports, level = [], 0
            for s in stable_bricks:
                if (s.start[0] <= brick.end[0] and brick.start[0] <= s.end[0]
                        and s.start[1] <= brick.end[1] and
                        brick.start[1] <= s.end[1]):
                    s_top = s.floor + s.height
                    if s_top > level:
                        supports, level = [], s_top
                    if s_top == level:
                        supports.append(s)
            brick.supports = supports
            brick.floor = level + 1
            for supp in supports:
                supp.supporting.append(brick)

        stable_bricks.append(brick)
    return stable_bricks


def part_one(stable_bricks):
    return sum(brick.safely_disintegrate() for brick in stable_bricks)


def part_two(stable_bricks):
    return sum(brick.would_fall() for brick in stable_bricks)


_list = []
with open(FILENAME) as file:
    lines = [line.strip().split('~') for line in file]
    for a, b in lines:
        _list.append([list(map(int, a.split(','))),
                      list(map(int, b.split(',')))])
bricks = [Brick(coords) for coords in _list]
stable_bricks = drop(bricks)
print(f'Part 1 - # of safe bricks: {part_one(stable_bricks)}')
print(f'Part 2 - sum of fallen bricks: {part_two(stable_bricks)}')
