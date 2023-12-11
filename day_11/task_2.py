def main():
    expansion = 1e6
    with open('input.txt', 'r') as file:
        galaxies = {}
        lines = file.readlines()
        add_y = 0
        for y, line in enumerate(lines):
            line = line.strip()
            if all([char == '.' for char in line]):
                add_y += 1
            else:
                inline_galaxies = [(x, y) for x, char in enumerate(line) if char == '#']
                for galaxy in inline_galaxies:
                    galaxies[galaxy] = add_y

        lines = list(zip(*lines))
        add_x = 0
        for x, line in enumerate(lines):
            if all([char == '.' for char in line]):
                add_x += 1
            else:
                inline_galaxies = [(x, y) for y, char in enumerate(line) if char == '#']
                for galaxy in inline_galaxies:
                    galaxies[galaxy] = (add_x * (expansion - 1), galaxies[galaxy] * (expansion - 1))

    list_galaxies = []
    for key, value in galaxies.items():
        list_galaxies.append((key[0] + value[0], key[1] + value[1]))

    distance_sum = 0
    counter = 0
    for i, _ in enumerate(list_galaxies):
        for j in range(i + 1, len(list_galaxies)):
            distance_sum += distance(list_galaxies[i], list_galaxies[j])
            counter += 1
    print(distance_sum)


def distance(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


if __name__ == '__main__':
    main()
