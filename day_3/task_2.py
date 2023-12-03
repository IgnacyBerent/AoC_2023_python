import numpy as np

from task_1 import find_numbers


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
            for xpos in find_stars(matrix_line)
        ]
        gears_numbers = find_gear_numbers(numbers_coords, symbols_coors)
        print(calc_gear_ratios(gears_numbers))


def find_stars(line: list[str]) -> list[int]:
    symbols_positions = []
    for i, char in enumerate(line):
        if char == '*':
            symbols_positions.append(i)
    return symbols_positions


def find_gear_numbers(
        numbers: list[dict[tuple[int, int]: int]],
        symbols_cords: list[tuple[int, int]]
) -> list[tuple[int, tuple[int, int]]]:
    gear_numbers = []
    for num_with_coords in numbers:
        for coords, num in num_with_coords.items():
            xpos, ypos = coords
            num_lenght = len(str(num))
            for add_y in [-1, 0, 1]:
                for add_x in range(-1, num_lenght + 1):
                    if (xpos + add_x, ypos + add_y) in symbols_cords:
                        gear_numbers.append((num, (xpos + add_x, ypos + add_y)))

    return gear_numbers


def calc_gear_ratios(gear_numbers: list[tuple[int, tuple[int, int]]]) -> int:
    numbers = [gear[0] for gear in gear_numbers]
    coords = [gear[1] for gear in gear_numbers]
    ratios = []
    for i, number in enumerate(numbers):
        for j in range(i + 1, len(numbers)):
            if coords[i] == coords[j]:
                ratios.append(number * numbers[j])
    return sum(ratios)


if __name__ == "__main__":
    main()
