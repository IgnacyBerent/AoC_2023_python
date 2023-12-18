from collections import defaultdict

directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

grid = defaultdict(lambda: defaultdict(lambda: 0))


def main():
    with open("input.txt", 'r') as file:
        lines = file.readlines()

    curr_pos = (0, 0)

    for line in lines:
        direction, length, color = line.strip().split()
        color = color[2:-1]
        for _ in range(int(length)):
            curr_pos = tuple(map(sum, zip(curr_pos, directions[direction])))
            grid[curr_pos[0]][curr_pos[1]] = color

    total = 0

    for y in range(max(grid.keys())+1):
        count = False
        if grid[y]:
            for x in range(max(grid[y].keys())+1):
                if grid[y][x] != 0:
                    total += 1
                    if ((grid[y + 1][x] != 0 and grid[y - 1][x] != 0)  # |
                            or (grid[y + 1][x] != 0 and grid[y][x + 1] != 0)  # F
                            or (grid[y + 1][x] != 0 and grid[y][x - 1] != 0)):  # 7
                        count = not count
                elif count:
                    total += 1
    print(total)


if __name__ == "__main__":
    main()
