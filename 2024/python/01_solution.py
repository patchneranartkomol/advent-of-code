from collections import Counter
FILENAME = 'input.txt'

l1, l2 = [], []
with open(FILENAME) as file:
    for line in file:
        w1, w2 = line.split()
        l1.append(int(w1))
        l2.append(int(w2))

def part_one(l1, l2):
    return sum(abs(n1 - n2) for n1, n2 in zip(sorted(l1), sorted(l2)))

print(f'Part 1: Total distance between lists: {part_one(l1, l2)}')

def part_two(l1, l2):
    counts = Counter(l2)
    return sum(n * counts[n] for n in l1)

print(f'Part 2: Similarity score: {part_two(l1, l2)}')
