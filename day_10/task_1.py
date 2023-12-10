pipes = {
    '|': ('N', 'S'),
    '-': ('E', 'W'),
    'L': ('N', 'E'),
    'J': ('N', 'W'),
    '7': ('S', 'W'),
    'F': ('S', 'E'),
    '.': None,
    'S': 'START',
}

directions = {
    'N': (0, -1),
    'S': (0, 1),
    'E': (1, 0),
    'W': (-1, 0),
}

antagonist_dir = {
    'N': 'S',
    'S': 'N',
    'E': 'W',
    'W': 'E',
}

area = []


def main():
    global area
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            area.append(list(line.strip()))
    start = None
    for y, line in enumerate(area):
        for x, char in enumerate(line):
            if char == 'S':
                start = (x, y)
                break

    # reshape columns with rows in area
    area = list(zip(*area))

    steps_direction = []
    for s_dir in 'NSEW':
        steps_direction.append(find_loop_len(start, s_dir))
    # delete None values
    steps_direction = list(filter(None, steps_direction))
    print(min(steps_direction)//2)


def find_loop_len(start, curr_dir) -> int | None:
    global area
    x, y = start
    x += directions[curr_dir][0]
    y += directions[curr_dir][1]
    steps = 1
    while True:
        if area[x][y] == '.':
            return None
        if area[x][y] == 'S':
            return steps
        if antagonist_dir[curr_dir] not in pipes[area[x][y]]:
            return None
        else:
            curr_dir = pipes[area[x][y]][0] if pipes[area[x][y]][0] != antagonist_dir[curr_dir] else pipes[area[x][y]][1]
            x += directions[curr_dir][0]
            y += directions[curr_dir][1]
            steps += 1


if __name__ == '__main__':
    main()
