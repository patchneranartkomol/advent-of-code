import heapq

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
        # Process last elf
        max_cals = max(curr_cals, max_cals)

    print(f'Part 1, top cals carried by any single elf: {max_cals}')

    # Part 2
    curr_cals = 0
    min_heap = [-1] * 3  # Store top 3 counts in min heap

    with open('../input/01_input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if line == '\n':
                if curr_cals > min_heap[0]:
                    heapq.heappushpop(min_heap, curr_cals)
                curr_cals = 0
            else:
                curr_cals += int(line)
        if curr_cals > min_heap[0]:
            heapq.heappushpop(min_heap, curr_cals)

    print(f'Part 2, total cals for top 3 elves: {sum(min_heap)}')
