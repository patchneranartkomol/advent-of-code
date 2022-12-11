from dataclasses import dataclass
from functools import reduce
from typing import Callable
from operator import mul


@dataclass
class Monkey:
    items: list[int]
    operation: Callable
    test: int
    succeed: int
    fail: int
    inspection_count: int


def execute_round(monkeys: list[Monkey]) -> None:
    for m in monkeys:
        for item in m.items:
            m.inspection_count += 1
            worry = m.operation(item)
            worry //= 3
            target = m.succeed if (worry % m.test == 0) else m.fail
            monkeys[target].items.append(worry)
        m.items.clear()


def execute_p2_round(monkeys: list[Monkey], factor: int) -> None:
    for m in monkeys:
        for item in m.items:
            m.inspection_count += 1
            worry = m.operation(item)
            worry %= factor
            target = m.succeed if (worry % m.test == 0) else m.fail
            monkeys[target].items.append(worry)
        m.items.clear()


def function_factory(op_str: str) -> Callable:
    tokens = op_str.split(' ')
    op = tokens[-2]
    try:
        operand = int(tokens[-1])
    except ValueError:
        operand = None
    match op:
        case '*':
            return (lambda x: x * operand) if operand else (lambda x: x * x)
        case '+':
            return (lambda x: x + operand) if operand else (lambda x: x + x)
        case _:
            raise RuntimeError("Unexpected Monkey Inspection operator")


def read_input(monkeys: list[Monkey]) -> None:
    with open('../input/11_input.txt', 'r', encoding='utf-8') as f:
        lines = [line.strip('\n') for line in f.readlines()]
        for i in range(0, len(lines), 7):
            starting_items = list(map(int, lines[i + 1].split(': ')[-1].split(', ')))
            f = function_factory(lines[i + 2].split(": ")[-1])
            test = int(lines[i + 3].split(' ')[-1])
            succeed = int(lines[i + 4].split(' ')[-1])
            fail = int(lines[i + 5].split(' ')[-1])
            monkeys.append(Monkey(starting_items, f, test, succeed, fail, 0))


monkeys = []
read_input(monkeys)
   
for _ in range(20):
    execute_round(monkeys)
monkeys.sort(key=lambda m: m.inspection_count, reverse=True)
mb = monkeys[0].inspection_count * monkeys[1].inspection_count
print(f'Part 1: Monkey Business {mb}')

monkeys = []
read_input(monkeys)

# Find common factor in modulo tests for all monkeys
factor = reduce(mul, (m.test for m in monkeys), 1)
for _ in range(10000):
    execute_p2_round(monkeys, factor)
monkeys.sort(key=lambda m: m.inspection_count, reverse=True)
mb = monkeys[0].inspection_count * monkeys[1].inspection_count
print(f'Part 2: Monkey Business {mb}')
