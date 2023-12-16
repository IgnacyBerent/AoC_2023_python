directions = {
    'u': (-1, 0),
    'r': (0, 1),
    'd': (1, 0),
    'l': (0, -1)
}
# \
back_slash_turns = {
    'u': 'l',
    'r': 'd',
    'd': 'r',
    'l': 'u'
}
# /
forward_slash_turns = {
    'u': 'r',
    'r': 'u',
    'd': 'l',
    'l': 'd'
}


def main():
    with open('input.txt', 'r') as file:
        contraption = [line.replace('\\', '7').strip() for line in file]

    print(beam_simulator(pos=(0, -1), direction='r', contraption=contraption))


def beam_simulator(pos: tuple[int, int], direction: str, contraption: list[str]) -> int:
    energized_tiles = set()
    visited_positions = set()
    stack = [(pos, direction)]

    while stack:
        pos, direction = stack.pop()
        d = directions[direction]
        new_pos = (pos[0] + d[0], pos[1] + d[1])

        if new_pos[0] < 0 or new_pos[1] < 0 or new_pos[0] >= len(contraption) or new_pos[1] >= len(contraption[0]):
            continue
        else:
            if (new_pos, direction) in visited_positions:
                continue
            visited_positions.add((new_pos, direction))
            energized_tiles.add(new_pos)
            if contraption[new_pos[0]][new_pos[1]] == '.':
                stack.append((new_pos, direction))
            elif contraption[new_pos[0]][new_pos[1]] == '7':
                stack.append((new_pos, back_slash_turns[direction]))
            elif contraption[new_pos[0]][new_pos[1]] == '/':
                stack.append((new_pos, forward_slash_turns[direction]))
            elif contraption[new_pos[0]][new_pos[1]] == '|':
                if direction == 'u' or direction == 'd':
                    stack.append((new_pos, direction))
                else:
                    stack.append((new_pos, 'd'))
                    stack.append((new_pos, 'u'))
            elif contraption[new_pos[0]][new_pos[1]] == '-':
                if direction == 'l' or direction == 'r':
                    stack.append((new_pos, direction))
                else:
                    stack.append((new_pos, 'l'))
                    stack.append((new_pos, 'r'))

    return len(energized_tiles)


if __name__ == '__main__':
    main()
