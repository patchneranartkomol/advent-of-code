from functools import cache
FILENAME = 'input.txt'
SYMBOLS = {'.', '#'}


class Row:
    def __init__(self, line):
        self.conditions, groups = line.split(' ')
        self.groups = tuple(i for i in map(int, groups.split(',')))
        self.expanded_conditions = '?'.join(self.conditions for _ in range(5))
        self.expanded_groups = tuple(self.groups * 5)


@cache
def count_unique_arrangements(seq, groups, curr_size=0):
    # Base case - entire string has been read and groups exhausted
    if not seq:
        return not groups and not curr_size
    cnt = 0
    # Recursive cases - continue iterating on the next character
    # Try either symbol when '?', or just first char if fixed
    possible_symbols = SYMBOLS if seq[0] == '?' else seq[0]
    for sym in possible_symbols:
        if sym == '.':
            if not curr_size:
                cnt += count_unique_arrangements(seq[1:], groups)
            else:
                if groups and groups[0] == curr_size:
                    cnt += count_unique_arrangements(seq[1:], groups[1:])
        else:
            cnt += count_unique_arrangements(seq[1:], groups, curr_size + 1)
    return cnt


def part_one(records):
    # Add '.' to ensure we hit the base case for our memoized recursion
    return sum(count_unique_arrangements(record.conditions + '.',
                                         record.groups) for record in records)


def part_two(records):
    return sum(count_unique_arrangements(record.expanded_conditions + '.',
                                         record.expanded_groups)
               for record in records)


records = []
with open(FILENAME) as file:
    for line in file:
        records.append(Row(line.strip()))
print(f'Part 1 - sum of unique arrangements: {part_one(records)}')
print(f'Part 2 - sum of unique arrangements: {part_two(records)}')
