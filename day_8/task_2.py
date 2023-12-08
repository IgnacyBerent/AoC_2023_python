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

        print(simul_run_steps_to_endpoint())


def find_z(start_pos, current_steps) -> tuple[str, int]:
    global maps, instructions
    for i, instruction in enumerate(instructions):
        if instruction == 'L':
            start_pos = maps[start_pos][0]
        elif instruction == 'R':
            start_pos = maps[start_pos][1]
        if start_pos[-1] == 'Z':
            return start_pos, i + 1 + current_steps
    return start_pos, len(instructions)+current_steps




def simul_run_steps_to_endpoint() -> int:
    all_starting_positions = list(filter(lambda pos: pos[-1] == 'A', maps))
    all_starts_steps = [0] * len(all_starting_positions)

    while True:
        for i, start in enumerate(all_starting_positions):
            if any(
                    current_step > all_starts_steps[i]
                    or all(steps == all_starts_steps[i] for steps in all_starts_steps)
                    for current_step in all_starts_steps
            ):
                all_starting_positions[i], all_starts_steps[i] = find_z(start, all_starts_steps[i])
                if all(
                        start[-1] == 'Z' and all_starts_steps[i] == steps
                        for start, steps
                        in zip(all_starting_positions, all_starts_steps)
                ):
                    return all_starts_steps[0]


if __name__ == '__main__':
    main()
