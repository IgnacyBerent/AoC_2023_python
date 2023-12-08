instructions = ''
maps = {}


def main():
    global maps, instructions
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if i == 0:
                instructions += line
            elif i != 1:
                current_pos, directions = line.split(' = ')
                directions = directions.strip()[1:-1].split(', ')
                maps[current_pos] = directions
        instructions = instructions.strip()

        endpoint_maps = {}
        for pos in maps:
            if pos != 'ZZZ':
                endpoint_maps[pos] = find_pos_after_instructions(pos)

        print(calc_steps_to_endpoint(endpoint_maps))


def find_pos_after_instructions(pos) -> tuple[str, int]:
    global maps, instructions
    for i, instruction in enumerate(instructions):
        if instruction == 'L':
            pos = maps[pos][0]
        elif instruction == 'R':
            pos = maps[pos][1]
        if pos == 'ZZZ':
            return 'ZZZ', i + 1

    return pos, len(instructions)


def calc_steps_to_endpoint(endpoint_maps):
    curr = 'AAA'
    all_steps = 0
    while True:
        curr, steps = endpoint_maps[curr]
        all_steps += steps
        if curr == 'ZZZ':
            return all_steps


if __name__ == '__main__':
    main()
