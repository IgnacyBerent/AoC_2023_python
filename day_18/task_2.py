from task_1 import area

directions = {
    "3": (-1, 0),
    "1": (1, 0),
    "2": (0, -1),
    "0": (0, 1),
}

hex_to_decimal = {
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15,
}


def hex_to_dec(hexn: str) -> int:
    """
    Convert hexadecimal number to decimal
    :param hexn: number in hexadecimal system
    :return: number in decimal system
    """
    result = 0
    for i, char in enumerate(reversed(hexn)):
        if char.isalpha():
            result += hex_to_decimal[char] * 16 ** i
        else:
            result += int(char) * 16 ** i
    return result


def main():
    with open("input.txt", 'r') as file:
        lines = file.readlines()

    points = []
    curr_pos = (0, 0)

    for line in lines:
        _, __, color = line.strip().split()
        color = color[2:-1]
        length = hex_to_dec(color[:-1])
        direction = directions[color[-1]]
        for _ in range(int(length)):
            curr_pos = tuple(map(sum, zip(curr_pos, direction)))
            points.append(curr_pos)

    print(area(points) + len(points) // 2 + 1)


if __name__ == "__main__":
    main()
