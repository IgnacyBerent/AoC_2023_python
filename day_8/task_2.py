import math
from functools import reduce

instructions = ''
maps = {}
endpoint_maps = {}
endpoint_z_maps = {}


def main():
    global maps, instructions, endpoint_maps, endpoint_z_maps
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

    map_z_to_z()
    print(endpoint_z_maps)

    all_starting_positions = list(filter(lambda pos: pos[-1] == 'A', maps))
    # for start_pos in all_starting_positions:
    #    end_pos, steps = find_z(start_pos)
    #    print(end_pos, steps)
    """
    It turns out that to every start A point is unique end Z point,
    number of starts is equal to endpoints, and number of steps it takes
    to get to given Z point is actually the same number of given Z point to
    get to closest Z point which is actually the same Z point
    """

    to_z_steps = [x[1] for x in list(endpoint_z_maps.values())]
    print(lcm_list(to_z_steps))


def find_pos_after_instructions(pos: str) -> tuple[str, int]:
    global maps, instructions
    for i, instruction in enumerate(instructions):
        if instruction == 'L':
            pos = maps[pos][0]
        elif instruction == 'R':
            pos = maps[pos][1]
        if pos[-1] == 'Z':
            return pos, i + 1

    return pos, len(instructions)


def find_z(start: str) -> tuple[str, int]:
    """
    number of steps to get to any z endpoint
    from given starting position
    :param start: a starting position
    :return: z endpoint, number of steps to get to it
    """
    global endpoint_maps
    curr = start
    all_steps = 0
    while True:
        curr, steps = endpoint_maps[curr]
        all_steps += steps
        if curr[-1] == 'Z':
            return curr, all_steps


def map_z_to_z():
    """
    makes global dictionary of number of steps
    that takes to get from one z endpoint to another
    """
    global endpoint_z_maps
    all_z_endpoints = list(filter(lambda pos: pos[-1] == 'Z', maps))
    for z_endpoint in all_z_endpoints:
        end_z, steps = find_z(z_endpoint)
        endpoint_z_maps[z_endpoint] = (end_z, steps)


def lcm(a: int, b: int) -> int:
    """
    Calculates least common multiple of two numbers
    :param a: number 1
    :param b: number 2
    :return: least common multiple of a and b
    """
    return abs(a * b) // math.gcd(a, b)


def lcm_list(numbers: list[int]) -> int:
    """
    Calculates least common multiple of list of numbers
    :param numbers: list of numbers
    :return: the least common multiple
    """
    return reduce(lcm, numbers)


if __name__ == '__main__':
    main()
