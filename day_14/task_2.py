from functools import lru_cache


def main():
    with open('input.txt', 'r') as file:
        data_platform = file.readlines()
    data_platform = tuple(tuple(line.strip()) for line in data_platform)
    for j in range(100):
        print(j, '%')
        for i in range(10_000_000):
            data_platform = cycle(data_platform)
    result = calc_weight(data_platform)
    print(result)


@lru_cache(maxsize=None)
def move_platform(data_platform: tuple[tuple[str]]) -> tuple[tuple[str]]:
    data_platform = list(list(line) for line in data_platform)
    shifts = 0
    for y, line in enumerate(data_platform):
        for x, char in enumerate(line):
            if y > 0:
                if char == 'O':
                    if data_platform[y - 1][x] == '.':
                        shifts += 1
                        data_platform[y - 1][x] = 'O'
                        data_platform[y][x] = '.'
    if shifts == 0:
        return tuple(tuple(line) for line in data_platform)
    else:
        return move_platform(tuple(tuple(line) for line in data_platform))


@lru_cache(maxsize=None)
def cycle(data_platform: tuple[tuple[str]]) -> tuple[tuple[str]]:
    data_platform = move_platform(data_platform)
    # rotate platform by -90 degrees
    data_platform = [list(line) for line in zip(*data_platform[::-1])]
    data_platform = move_platform(tuple(tuple(line) for line in data_platform))
    # rotate platform by -90 degrees
    data_platform = [list(line) for line in zip(*data_platform[::-1])]
    data_platform = move_platform(tuple(tuple(line) for line in data_platform))
    # rotate platform by -90 degrees
    data_platform = [list(line) for line in zip(*data_platform[::-1])]
    data_platform = move_platform(tuple(tuple(line) for line in data_platform))
    # rotate platform by -90 degrees
    data_platform = [list(line) for line in zip(*data_platform[::-1])]
    return tuple(tuple(line) for line in data_platform)


def calc_weight(data_platform: tuple[tuple[str]]) -> int:
    data_platform = list(list(line) for line in reversed(data_platform))
    weight = sum([y + 1 for y, line in enumerate(data_platform)
                  for x, char in enumerate(line)
                  if char == 'O'])
    return weight


if __name__ == '__main__':
    main()
