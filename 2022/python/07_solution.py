from typing import Optional

TOTAL_SPACE = 70000000
SPACE_NEEDED = 30000000
total1 = 0
dirs = []

class Directory:
    count = 0
    def __init__(self, parent: Optional['Directory'], name) -> None:
        self.parent = parent
        self.name = name
        self.files = []
        self.children = []
        self.size = -1

    def sum_size_100000(self) -> int:
        size = 0
        for child in self.children:
            c_size = child.sum_size_100000()
            size += c_size
        global total1
        size += sum(f.size for f in self.files)
        if size < 100000:
            total1 += size
        # Annotate this node to save work in part 2
        self.size = size
        global dirs
        dirs.append(self)
        return size


class File:
    def __init__(self, size: int, name: str) -> None:
        self.size = size
        self.path = name

    
if __name__ == '__main__':
    with open('../input/07_input.txt', 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]

    parent = Directory(None, '')
    # Populate root directory - Entered into by '$ cd /'
    parent.children.append(Directory(None, '/'))
    c_dir = parent
    i = 0
    while i < len(lines):
        tokens = lines[i].split(' ')
        assert tokens[0] == '$'
        match tokens[1]:
            case 'ls':
                i += 1
                while i < len(lines) and not lines[i].startswith('$'):
                    a, b = lines[i].split(' ')
                    if a == 'dir':
                        c_dir.children.append(Directory(c_dir, b))
                    else:
                        c_dir.files.append(File(int(a), b))
                    i += 1
            case 'cd':
                if tokens[2] == '..':
                    c_dir = c_dir.parent
                else:
                    target = next(d for d in c_dir.children if d.name == tokens[2])
                    c_dir = target
                i += 1

    root = parent.children[0]
    root.sum_size_100000()
    print(f'Part 1: Sum of directories with sizes less than 100,000: {total1}')
    free_space = TOTAL_SPACE - root.size 
    min_delete = SPACE_NEEDED - free_space
    for d in sorted(dirs, key=lambda x: x.size):
        if d.size > min_delete:
            print(f'Part 2: Total size of directory to free: {d.size}')
            break
