import math
from collections import namedtuple

FILENAME = 'input.txt'
MAP_COUNT = 7
MapRange = namedtuple('MapRange', ['dest_start', 'source_start', 'length'])


class Map:
    def __init__(self, source_category, destination_category, ranges):
        self.source_category = source_category
        self.destination_category = destination_category
        self.ranges = sorted(ranges, key=lambda x: x.source_start)


def convert(loc, _map):
    for r in _map.ranges:
        if r.source_start <= loc < r.source_start + r.length:
            return r.dest_start - r.source_start + loc
    return loc


def part_one(seeds, maps):
    min_loc = math.inf
    for seed in seeds:
        loc = seed
        for _map in maps:
            loc = convert(loc, _map)
        min_loc = min(min_loc, loc)
    return min_loc


# Brute force
def part_two(seeds, maps):
    min_loc = math.inf
    seed_ranges, i = [], 0
    while i < len(seeds):
        seed_ranges.append(range(seeds[i], seeds[i] + seeds[i + 1]))
        i += 2
    for r in seed_ranges:
        for seed in r:
            loc = seed
            for _map in maps:
                loc = convert(loc, _map)
            min_loc = min(min_loc, loc)
    return min_loc


with open(FILENAME) as file:
    seeds = [int(s) for s in file.readline().split(':')[1].strip().split(' ')]
    maps = []

    assert file.readline() == '\n'
    for i in range(MAP_COUNT):
        ranges = []
        map_name = file.readline().split(' ')[0]
        while True:
            line = file.readline().strip()
            if len(line) == 0:
                break
            dest_start, source_start, length = map(int, line.split(' '))
            ranges.append(MapRange(dest_start=dest_start,
                                   source_start=source_start, length=length))

        source_category, _, destination_category = map_name.split('-')
        maps.append(Map(source_category, destination_category, ranges))


print(f'Part 1: lowest location number: {part_one(seeds, maps)}')
print(f'Part 2: lowest location number: {part_two(seeds, maps)}')
