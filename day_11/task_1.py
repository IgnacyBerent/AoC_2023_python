from itertools import chain


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        galaxies = []
        galaxies_map = []
        for y, line in enumerate(lines):
            line = line.strip()
            if all([char == '.' for char in line]):
                galaxies_map.append(line)
            galaxies_map.append(line)

        galaxies_map = list(zip(*galaxies_map))
        add_x = 0
        for x, line in enumerate(galaxies_map):
            if all([char == '.' for char in line]):
                add_x += 1
            else:
                galaxies.append([(x + add_x, y) for y, char in enumerate(line) if char == '#'])

    galaxies = list(chain.from_iterable(galaxies))
    distance_sum = 0
    counter = 0
    for i, _ in enumerate(galaxies):
        for j in range(i + 1, len(galaxies)):
            distance_sum += distance(galaxies[i], galaxies[j])
            counter += 1
    print(distance_sum)


def distance(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


if __name__ == '__main__':
    main()
