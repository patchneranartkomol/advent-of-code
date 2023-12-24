from collections import defaultdict, deque
FILENAME = 'input.txt'


def button(module_map):
    high = low = 0
    messages = deque()
    messages.append(('button', 'low', 'broadcaster'))
    while messages:
        sender, pulse, curr = messages.popleft()
        if pulse == 'low':
            low += 1
        else:
            high += 1
        module = module_map[curr]
        destinations = module.destinations

        if module.type == 'broadcaster':
            msg_type = pulse
            for d in destinations:
                messages.append((module.name, msg_type, d))
        elif module.type == '%':
            if pulse == 'low':
                msg_type = 'high' if module.status == 0 else 'low'
                for d in destinations:
                    messages.append((module.name, msg_type, d))
                module.status ^= 1
        elif module.type == '&':
            module.status[sender] = 0 if pulse == 'low' else 1
            msg_type = 'low' if all(module.status.values()) == 1 else 'high'
            for d in destinations:
                messages.append((module.name, msg_type, d))
    return high, low


def part_one(module_map):
    high = low = 0
    for _ in range(1000):
        hp, lp = button(module_map)
        high += hp
        low += lp
    return high * low


class Module:
    def __init__(self, name, _type, destinations):
        self.name = name
        self.type = _type
        self.destinations = destinations
        if self.type == '%':
            self.status = 0
        elif self.type == '&':
            self.status = defaultdict(int)


modules = []
with open(FILENAME) as file:
    for line in file:
        config, dest = line.strip().split(' -> ')
        if config == 'broadcaster':
            _type = config
            name = config
        else:
            _type = config[0]
            name = config[1:]
        destinations = dest.split(', ')
        modules.append(Module(name, _type, destinations))

module_map = {m.name: m for m in modules}
for m in modules:
    for d in m.destinations:
        # Add untyped modules - i.e. 'output' or 'rx'
        if d not in module_map:
            module_map[d] = Module(d, 'untyped', [])
        # Initialize all destinations to 0 for conjunction modules
        elif module_map[d].type == '&':
            module_map[d].status[m.name] = 0
print(f'Part 1 - low * high pulses sent: {part_one(module_map)}')
