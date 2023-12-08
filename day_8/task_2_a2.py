instructions = ''
maps = {}
endpoint_maps = {}


def main():
    global maps, instructions, endpoint_maps
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

    for pos in maps:
        endpoint_maps[pos] = find_pos_after_instructions(pos)

    all_starting_positions = list(filter(lambda pos: pos[-1] == 'A', maps))
    all_z_locations = []
    for start_pos in all_starting_positions:
        pos = start_pos
        steps_for_start = []
        for j in range(10000000):
            pos, t_steps = calc_steps_to_endpoint(pos)
            steps_for_start.append(t_steps)
        all_z_locations.append(steps_for_start)

    for loc in all_z_locations:
        for i in range(1, len(loc)):
            loc[i] += loc[i - 1]

    # make intersecion of values of lists
    result_sets = list(map(set, all_z_locations))
    result = min(set.intersection(*result_sets))
    print(result)


def find_pos_after_instructions(pos) -> tuple[str, int]:
    global maps, instructions
    for i, instruction in enumerate(instructions):
        if instruction == 'L':
            pos = maps[pos][0]
        elif instruction == 'R':
            pos = maps[pos][1]
        if pos[-1] == 'Z':
            return pos, i + 1

    return pos, len(instructions)


def calc_steps_to_endpoint(start):
    global endpoint_maps
    curr = start
    all_steps = 0
    while True:
        curr, steps = endpoint_maps[curr]
        all_steps += steps
        if curr[-1] == 'Z':
            return curr, all_steps


if __name__ == '__main__':
    main()
