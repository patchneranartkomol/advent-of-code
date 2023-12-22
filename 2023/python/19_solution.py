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


def part_one(workflows, parts):
    w_map = {w.name: w for w in workflows}
    accepted_parts = []
    for part in parts:
        if check_part(part, w_map):
            accepted_parts.append(part)
    return sum(sum(p.values()) for p in accepted_parts)


with open(FILENAME) as file:
    lines = [line.strip() for line in file]
mid = lines.index('')
workflows = [Workflow(line) for line in lines[:mid]]
parts = []
for ln in lines[mid + 1:]:
    x, m, a, s = map(lambda s: int(s.split('=')[1]), ln.strip('{}').split(','))
    parts.append({'x': x, 'm': m, 'a': a, 's': s})
print(f'Part 1 - sum of all accepted ratings: {part_one(workflows, parts)}')
