UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)

downhill = {
    UP: '^',
    DOWN: 'v',
    LEFT: '<',
    RIGHT: '>'
}


def main(file: str):
    with open(file, 'r') as f:
        forest = [list(line.strip()) for line in f.readlines()]

    forest[0][1] = '#'
    start = (1, 1)
    end = (len(forest) - 1, len(forest[0]) - 2)
    v = set()
    v.add(start)

    stack = [((1, 1), v, False)]
    finished = []

    while stack:
        curr_pos, visited, step_on_slope = stack.pop()

        for dir in [UP, DOWN, LEFT, RIGHT]:
            new_pos = (curr_pos[0] + dir[0], curr_pos[1] + dir[1])
            if new_pos == end:
                visited.add(new_pos)
                finished.append(visited)
                continue
            if new_pos in visited:
                continue
            if forest[new_pos[0]][new_pos[1]] == '#':
                continue
            new_visited = visited.copy()
            if step_on_slope:
                if forest[new_pos[0]][new_pos[1]] == downhill[dir]:
                    new_visited.add(new_pos)
                    new_pos = (new_pos[0] + dir[0], new_pos[1] + dir[1])
                    new_visited.add(new_pos)
                    stack.append((new_pos, new_visited, False))
            else:
                if forest[new_pos[0]][new_pos[1]] in ['<', '>', '^', 'v']:
                    new_visited.add(new_pos)
                    new_pos = (new_pos[0] + dir[0], new_pos[1] + dir[1])
                    new_visited.add(new_pos)
                    stack.append((new_pos, new_visited, True))
                else:
                    new_visited.add(new_pos)
                    stack.append((new_pos, new_visited, False))

    print(max([len(visit) for visit in finished]))


if __name__ == '__main__':
    main('input.txt')
