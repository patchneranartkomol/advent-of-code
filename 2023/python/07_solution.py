from collections import Counter
FILENAME = 'input.txt'
TYPE_STRENGTH_MAP = {
    'five-of-a-kind': 7,
    'four-of-a-kind': 6,
    'full-house': 5,
    'three-of-a-kind': 4,
    'two-pair': 3,
    'one-pair': 2,
    'high-card': 1,
}
# Part one rules
CARD_STRENGTH_MAP = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}
# Part two rules
JOKER_MAP = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'J': 1,
}


class Hand:
    card_strength_map = CARD_STRENGTH_MAP

    def __init__(self, line):
        self.cards, self.bid = line.split()
        self.bid = int(self.bid)
        self.parse_hand_type()

    def parse_hand_type(self):
        counts = Counter(self.cards)
        if len(counts.keys()) == 1:
            self.type = 'five-of-a-kind'
        elif len(counts.keys()) == 5:
            self.type = 'high-card'
        elif len(counts.keys()) == 4:
            self.type = 'one-pair'
        elif len(counts.keys()) == 2:
            if max(counts.values()) == 4:
                self.type = 'four-of-a-kind'
            else:
                self.type = 'full-house'
        else:
            if max(counts.values()) == 3:
                self.type = 'three-of-a-kind'
            else:
                self.type = 'two-pair'

    def __repr__(self):
        return f"{type(self).__name__}({self.cards}, {self.bid}, {self.type})"

    def __lt__(self, other):
        if self.type != other.type:
            return TYPE_STRENGTH_MAP[self.type] < TYPE_STRENGTH_MAP[other.type]
        for char, otr_char in zip(self.cards, other.cards):
            if char != otr_char:
                return self.card_strength_map[char] < \
                    self.card_strength_map[otr_char]
        raise RuntimeError('Unexpected comparison - cards are equal')


class JokerHand(Hand):
    card_strength_map = JOKER_MAP

    def parse_hand_type(self):
        counts = Counter(self.cards)
        if counts['J'] and counts['J'] != 5:
            j_count = counts['J']
            del counts['J']
            max_count = max(counts.values())
            for k in counts:
                if counts[k] == max_count:
                    counts[k] += j_count
                    break

        if len(counts.keys()) == 1:
            self.type = 'five-of-a-kind'
        elif len(counts.keys()) == 5:
            self.type = 'high-card'
        elif len(counts.keys()) == 4:
            self.type = 'one-pair'
        elif len(counts.keys()) == 2:
            if max(counts.values()) == 4:
                self.type = 'four-of-a-kind'
            else:
                self.type = 'full-house'
        else:
            if max(counts.values()) == 3:
                self.type = 'three-of-a-kind'
            else:
                self.type = 'two-pair'


def calc(hands):
    total = 0
    for i, h in enumerate(sorted(hands)):
        total += (i + 1) * h.bid
    return total


lines = []
with open(FILENAME) as file:
    for line in file:
        lines.append(line.strip())
print(f'Part 1: total winnings: {calc((Hand(line) for line in lines))}')
print(f'Part 2: total winnings: {calc((JokerHand(line) for line in lines))}')
