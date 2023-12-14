def main():
    with open('input.txt', 'r') as file:
        data_platform = file.readlines()
    data_platform = [list(line.strip()) for line in data_platform]
    result = calc_weight(data_platform)
    print(result)


def move_platform(data_platform: list[list[str]]) -> list[list[str]]:
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
        return data_platform
    else:
        return move_platform(data_platform)


def calc_weight(data_platform: list[list[str]]) -> int:
    data_platform = list(reversed(move_platform(data_platform)))
    weight = sum([y+1 for y, line in enumerate(data_platform)
                  for x, char in enumerate(line)
                  if char == 'O'])
    return weight


if __name__ == '__main__':
    main()
