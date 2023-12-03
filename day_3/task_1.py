import numpy as np

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', '\\', ':',
           ';', '"', "'", '<', '>', ',', '?', '/', '`', '~']


def main():
    with open("input.txt") as file:
        lines = file.readlines()
        lines_matrix = np.array([list(line.strip()) for line in lines])
        numbers_coords = [
            {(xpos, y_pos): num}
            for y_pos, matrix_line in enumerate(lines_matrix)
            for xpos, num in find_numbers(matrix_line).items()
        ]
        symbols_coors = [
            (xpos, y_pos)
            for y_pos, matrix_line in enumerate(lines_matrix)
            for xpos in find_symbols(matrix_line)
        ]
        part_numbers = find_part_numbers(numbers_coords, symbols_coors)
        print(sum(part_numbers))


def find_numbers(line: list[str]) -> dict:
    numbers = []
    x_positions = []
    i = 0
    while i < len(line):
        whole_number = []
        if line[i].isdigit():
            x_positions.append(i)
            j = 0
            while j < 4:
                try:
                    line[i + j]
                except IndexError:
                    numbers.append(int(''.join(whole_number)))
                    break
                if line[i + j].isdigit():
                    whole_number.append(line[i + j])
                    j += 1
                else:
                    numbers.append(int(''.join(whole_number)))
                    break
            i += j
        else:
            i += 1

    return {pos: num for pos, num in zip(x_positions, numbers)}


def find_symbols(line: list[str]) -> list[int]:
    symbols_positions = []
    for i, char in enumerate(line):
        if char in symbols:
            symbols_positions.append(i)
    return symbols_positions


def find_part_numbers(
        numbers: list[dict[tuple[int, int]: int]],
        symbols_cords: list[tuple[int, int]]
) -> list[int]:

    part_numbers = []
    for num_with_coords in numbers:
        for coords, num in num_with_coords.items():
            xpos, ypos = coords
            num_lenght = len(str(num))
            for add_y in [-1, 0, 1]:
                found = False
                for add_x in range(-1, num_lenght + 1):
                    if (xpos + add_x, ypos + add_y) in symbols_cords:
                        part_numbers.append(num)
                        found = True
                        break
                if found: break
    return part_numbers


if __name__ == "__main__":
    main()
