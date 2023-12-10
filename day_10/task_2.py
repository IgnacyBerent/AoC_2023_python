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
clear_area = []


def main():
    global area, clear_area
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

    final_cords_w_dir = None
    for s_dir in 'NSEW':
        loop_cords = find_loop_cords(start, s_dir)
        if loop_cords:
            final_cords_w_dir = loop_cords
            break

    clear_area = []
    for x, line in enumerate(area):
        new_line = []
        for y, char in enumerate(line):
            if (x, y) in final_cords_w_dir:
                new_line.append(char)
            else:
                new_line.append('0')
        clear_area.append(new_line)

    # reshape columns with rows in area
    clear_area = list(zip(*clear_area))

    tiles = 0
    for y, line in enumerate(clear_area):
        count_tiles = False
        for x, char in enumerate(line):
            if char != '0':
                if (char == 'F' or char == '7' or char == '|' or char == 'S') and not count_tiles:
                    count_tiles = True
                elif (char == 'F' or char == '7' or char == '|' or char == 'S') and count_tiles:
                    count_tiles = False
            if char == '0' and count_tiles:
                tiles += 1
    print(tiles)


def find_loop_cords(start, curr_dir) -> list[tuple[int, int]] | None:
    global area
    loop_cords = [start]
    x, y = start
    x += directions[curr_dir][0]
    y += directions[curr_dir][1]
    loop_cords.append((x, y))
    while True:
        if area[x][y] == '.':
            return None
        if area[x][y] == 'S':
            return loop_cords
        if antagonist_dir[curr_dir] not in pipes[area[x][y]]:
            return None
        else:
            curr_dir = pipes[area[x][y]][0] if pipes[area[x][y]][0] != antagonist_dir[curr_dir] else pipes[area[x][y]][
                1]
            x += directions[curr_dir][0]
            y += directions[curr_dir][1]
            loop_cords.append((x, y))


if __name__ == '__main__':
    main()
