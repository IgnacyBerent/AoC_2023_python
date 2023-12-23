from collections import defaultdict


class Brick:
    def __init__(self, start: tuple, end: tuple):
        self.sx = start[0]
        self.sy = start[1]
        self.sz = start[2]
        self.ex = end[0]
        self.ey = end[1]
        self.ez = end[2]
        self.holds = set()
        self.held_by = set()

    def __repr__(self):
        return f'({self.sx}, {self.sy}, {self.sz}) ~ ({self.ex}, {self.ey}, {self.ez})'

    def __gt__(self, other):
        return self.sz > other.sz

    def __lt__(self, other):
        return self.sz < other.sz


platform = defaultdict(lambda: defaultdict(int))


def main(file: str):
    with open(file, 'r') as f:
        bricks = [
            (
                Brick(
                    tuple(map(int, start.split(','))),
                    tuple(map(int, end.split(',')))
                )
            ) for start, end in [
                line.strip().split('~') for line in f.readlines()
            ]
        ]
    bricks.sort()
    bricks = fall_bricks(bricks)
    bricks = find_holds(bricks)

    result = 0
    for brick in bricks:
        if brick.holds == set() or all(len(held.held_by) > 1 for held in brick.holds):
            result += 1

    print(result)


def fall_bricks(data_bricks):
    bricks = data_bricks.copy()
    for brick in bricks:
        if brick.sx != brick.ex:
            platform_height = max([platform[x][brick.sy] for x in range(brick.sx, brick.ex + 1)])
            for x in range(brick.sx, brick.ex + 1):
                platform[x][brick.sy] = platform_height + 1
                brick.sz = platform_height + 1
                brick.ez = platform_height + 1
        elif brick.sy != brick.ey:
            platform_height = max([platform[brick.sx][y] for y in range(brick.sy, brick.ey + 1)])
            for y in range(brick.sy, brick.ey + 1):
                platform[brick.sx][y] = platform_height + 1
                brick.sz = platform_height + 1
                brick.ez = platform_height + 1
        else:
            brick_height = abs(brick.ez - brick.sz)
            brick.sz = platform[brick.sx][brick.sy] + 1
            brick.ez = brick.sz + brick_height
            platform[brick.sx][brick.sy] += brick_height + 1
    return bricks

def find_holds(bricks):
    for brick in bricks:
        if brick.sx != brick.ex:
            # find all bricks over the brick
            for x in range(brick.sx, brick.ex + 1):
                for other_brick in bricks:
                    if (other_brick.sx <= x <= other_brick.ex
                            and other_brick.sy <= brick.sy <= other_brick.ey
                            and other_brick.sz == brick.ez + 1):
                        brick.holds.add(other_brick)
                        other_brick.held_by.add(brick)
        elif brick.sy != brick.ey:
            # find all bricks over the brick
            for y in range(brick.sy, brick.ey + 1):
                for other_brick in bricks:
                    if (other_brick.sy <= y <= other_brick.ey
                            and other_brick.sx <= brick.sx <= other_brick.ex
                            and other_brick.sz == brick.ez + 1):
                        brick.holds.add(other_brick)
                        other_brick.held_by.add(brick)
        else:
            # find all bricks over the brick
            for other_brick in bricks:
                if (other_brick.sx <= brick.sx <= other_brick.ex
                        and other_brick.sy <= brick.sy <= other_brick.ey
                        and other_brick.sz == brick.ez + 1):
                    brick.holds.add(other_brick)
                    other_brick.held_by.add(brick)
                    break
    return bricks

if __name__ == '__main__':
    main('input.txt')
