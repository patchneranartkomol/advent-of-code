from functools import cmp_to_key
from typing import Generator
import ast


def check(left: str, right: str) -> int:
    l, r = map(ast.literal_eval, (left, right))
    return _check(l, r)


def _check(left: list[int | list[int]], right: list[int | list[int]]) -> int:
    if type(left) == int and type(right) == list:
        return _check([left], right)
    elif type(left) == list and type(right) == int:
        return _check(left, [right])
    elif type(left) == type(right) == list:
        for l, r in zip(left, right):
            o = _check(l, r)
            if o != 0:
                return o
        return _check(len(left), len(right))
    elif left != right:
        return 1 if left < right else -1
    return 0


def group(_list: list[str]) -> Generator[list[str], None, None]:
    for i in range(0, len(_list), 2):
        yield [_list[i], _list[i + 1]]


with open('../input/13_input.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip('\n') for line in f.readlines() if line != '\n']

right_indices = set()
for i, pair in enumerate(p for p in group(lines)):
    if check(pair[0], pair[1]) == 1:
        right_indices.add(i + 1)

print(f'Part 1: sum of indices: {sum(right_indices)}')

lines.extend(['[[2]]', '[[6]]'])
lines.sort(key=cmp_to_key(check), reverse=True)
a, b = lines.index('[[2]]'), lines.index('[[6]]')
print(f'Part 2: {(a + 1) * (b + 1)}')
