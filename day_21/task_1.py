from collections import deque

dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
STEPS = 6


def main(file: str):
    with open(file, 'r') as f:
        lines = f.readlines()

    # determine starting coordinates
    start = None
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == 'S':
                start = (y, x)
                break

    rocks_cords = []
    # determine rocks coordinates
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                rocks_cords.append((y, x))

    curr_positions = deque([(0, start)])
    visited = set()
    final = set()

    while curr_positions:
        step, curr_pos = curr_positions.popleft()
        if step == STEPS:
            final.add(curr_pos)
            continue
        if curr_pos not in visited:
            new_poses = []
            for dir in dirs:
                new_pos = (curr_pos[0] + dir[0], curr_pos[1] + dir[1])
                # if not out of grid boundaries:
                if (0 <= new_pos[0] < len(lines) and 0 <= new_pos[1] < len(lines[0]) and new_pos not in rocks_cords):
                    if new_pos not in visited:
                        curr_positions.append((step + 1, new_pos))
                        visited.add(new_pos)
                        new_poses.append(new_pos)
                        if step % 2 == 0:
                            final.add(new_pos)

    print(len(final))


if __name__ == '__main__':
    main('example.txt')
