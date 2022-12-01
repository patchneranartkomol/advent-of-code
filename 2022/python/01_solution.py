from collections import Counter

if __name__ == '__main__':
    # Part 1
    curr_cals = max_cals = 0

    with open('../input/01_input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if line == '\n':
                max_cals = max(curr_cals, max_cals)
                curr_cals = 0
            else:
                curr_cals += int(line)
        max_cals = max(curr_cals, max_cals)
    print(f'Part 1, top cals carried by single elf: {max_cals}')

    # Part 2
    cal_counts = Counter()
    elf_count = total = 0
    curr_cals = 0

    with open('../input/01_input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if line == '\n':
                cal_counts[elf_count] = curr_cals
                curr_cals = 0
                elf_count += 1
            else:
                curr_cals += int(line)
        cal_counts[elf_count] = curr_cals

    for _, cals in cal_counts.most_common(3):
        total += cals

    print(f'Part 2, total cals for top 3 elves: {total}')
