from copy import deepcopy
FILENAME = 'input.txt'


class Workflow:
    def __init__(self, text):
        self.name, raw = text.split('{')
        rules = raw[:-1].split(',')
        self.rules = [self._parse_rule(rule) for rule in rules]

    def _parse_rule(self, rule):
        if ':' not in rule:
            return rule
        cond, dest = rule.split(':')
        return (cond[0], cond[1], int(cond[2:]), dest)


def check_part(part, w_map):
    rule = 'in'
    while rule not in {'A', 'R'}:
        workflow = w_map[rule]
        for r in workflow.rules:
            match r:
                case str():
                    rule = r
                    break
                case tuple():
                    sym, cond, val, dest = r
                    if cond == '<':
                        if part[sym] < val:
                            rule = dest
                            break
                    if cond == '>':
                        if part[sym] > val:
                            rule = dest
                            break
    return rule == 'A'


def part_one(w_map, parts):
    accepted_parts = []
    for part in parts:
        if check_part(part, w_map):
            accepted_parts.append(part)
    return sum(sum(p.values()) for p in accepted_parts)


def check_workflow(w_map, ranges, curr_rule):
    if curr_rule == 'A':
        possibilities = 1
        for _range in ranges.values():
            possibilities *= len(_range)
        return possibilities
    elif curr_rule == 'R':
        return 0

    count = 0
    for rule in w_map[curr_rule].rules:
        match rule:
            case str():
                count += check_workflow(w_map, ranges, rule)
            case tuple():
                sym, cond, val, dest = rule
                if cond == '<':
                    acc_branch = range(ranges[sym].start, int(val))
                    rej_branch = range(int(val), ranges[sym].stop)
                    accepted_ranges = deepcopy(ranges)
                    accepted_ranges[sym] = acc_branch
                    # Modify current to continue processing of rejected branch
                    ranges[sym] = rej_branch
                    count += check_workflow(w_map, accepted_ranges, dest)
                if cond == '>':
                    acc_branch = range(int(val) + 1, ranges[sym].stop)
                    rej_branch = range(ranges[sym].start, int(val) + 1)
                    accepted_ranges = deepcopy(ranges)
                    accepted_ranges[sym] = acc_branch
                    ranges[sym] = rej_branch
                    count += check_workflow(w_map, accepted_ranges, dest)
    return count


def part_two(w_map):
    w_map = {w.name: w for w in workflows}
    ranges = {k: range(1, 4001) for k in {'x', 'm', 'a', 's'}}
    return check_workflow(w_map, ranges, 'in')


with open(FILENAME) as file:
    lines = [line.strip() for line in file]
mid = lines.index('')
workflows = [Workflow(line) for line in lines[:mid]]
w_map = {w.name: w for w in workflows}
parts = []
for ln in lines[mid + 1:]:
    x, m, a, s = map(lambda s: int(s.split('=')[1]), ln.strip('{}').split(','))
    parts.append({'x': x, 'm': m, 'a': a, 's': s})
print(f'Part 1 - sum of all accepted ratings: {part_one(w_map, parts)}')
print(f'Part 2 - distinct accepted combinations: {part_two(w_map)}')
