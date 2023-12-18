directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}


def area(points: list[tuple[int, int]]) -> int:
    """
    Shoelace formula
    :param points: list of points
    :return: area of polygon
    """

    result = 0
    for i in range(len(points) - 1):
        y1, x1 = points[i]
        y2, x2 = points[i + 1]
        result += x1 * y2 - x2 * y1

    return abs(result) // 2


def main():
    with open("input.txt", 'r') as file:
        lines = file.readlines()

    points = []
    curr_pos = (0, 0)

    for line in lines:
        direction, length, _ = line.strip().split()
        for _ in range(int(length)):
            curr_pos = tuple(map(sum, zip(curr_pos, directions[direction])))
            points.append(curr_pos)

    # we use Pick's theorem to calculate number of interior points
    # A = i + b/2 - 1
    # where
    # A is area of polygon,
    # i is number of interior points,
    # b is number of boundary points
    # i + b = A - b/2 + 1
    print(area(points) + len(points) // 2 + 1)


if __name__ == "__main__":
    main()
