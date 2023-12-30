from collections import defaultdict
FILENAME = 'input.txt'


def count(v): return len(graph[v] - _set)


graph = defaultdict(set)

for line in open(FILENAME):
    u, *vs = line.replace(':', '').split()
    for v in vs:
        graph[u].add(v)
        graph[v].add(u)

# Set begins with all vertices of graph
_set = set(graph)

# Remove vertices in set by order of most neighbors until there are only 3
# Credit - /u/4HbQ for this ingenious solution
while sum(map(count, _set)) != 3:
    # It is possible for some runs of this code to evict
    # an element that should be in the set - resulting in an error
    _set.remove(max(_set, key=count))

print('Multiple of sized of 2 connected components after cut: ' +
      f'{len(_set) * len(set(graph) - _set)}')
