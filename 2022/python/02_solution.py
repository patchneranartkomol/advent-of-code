MOVES_SCORE1 = {
    # Opponent - Rock
    'A': {
        'X': 3 + 1, # Draw + Rock
        'Y': 6 + 2, # Win + Paper
        'Z': 0 + 3, # Lose + Scissors
    },
    # Opponent - Paper
    'B': {
        'X': 0 + 1, # Lose + Rock
        'Y': 3 + 2, # Draw + Paper
        'Z': 6 + 3, # Win + Scissors
    },
    # Opponent - Scissors
    'C': {
        'X': 6 + 1, # Win + Rock
        'Y': 0 + 2, # Lose + Paper
        'Z': 3 + 3, # Draw + Scissors
    },
}

MOVES_SCORE2 = {
    # Opponent - Rock
    'A': {
        'X': 0 + 3, # Lose => Scissors
        'Y': 3 + 1, # Draw => Rock
        'Z': 6 + 2, # Win => Paper
    },
    # Opponent - Paper
    'B': {
        'X': 0 + 1, # Lose => Rock
        'Y': 3 + 2, # Draw => Paper
        'Z': 6 + 3, # Win => Scissors
    },
    # Opponent - Scissors
    'C': {
        'X': 0 + 2, # Lose => Paper
        'Y': 3 + 3, # Draw => Scissors
        'Z': 6 + 1, # Win => Rock
    },
}

if __name__ == '__main__':
    total1 = 0
    with open('../input/02_input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            opponent, selected = line.strip().split(' ')
            total1 += MOVES_SCORE1[opponent][selected]
    
    print(f'Part 1: Total Score: {total1}')

    total2 = 0
    with open('../input/02_input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            opponent, selected = line.strip().split(' ')
            total2 += MOVES_SCORE2[opponent][selected]

    print(f'Part 2: Total Score: {total2}')
