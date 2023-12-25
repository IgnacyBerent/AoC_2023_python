LB = 200000000000000
HB = 400000000000000


class Hailstone:
    def __init__(self, position, velocity):
        self.x = position[0]
        self.y = position[1]
        self.vx = velocity[0]
        self.vy = velocity[1]
        self.a = None
        self.b = None
        self._calc_ab()

    def _calc_ab(self):
        self.a = self.vy / self.vx
        self.b = self.y - self.a * self.x

    def __repr__(self):
        return (f'({self.x}, {self.y}) @ ({self.vx}, {self.vy})\n {self.a}x + {self.b} = 0')


def main(file: str):
    with open(file, 'r') as f:
        hailstones = [
            (
                Hailstone(
                    tuple(map(int, start.split(','))),
                    tuple(map(int, end.split(',')))
                )
            ) for start, end in [
                line.strip().split('@') for line in f.readlines()
            ]
        ]

    result = 0
    for i, hailstone in enumerate(hailstones):
        for other_hailstone in hailstones[i + 1:]:
            if intersect_in_area(hailstone, other_hailstone):
                result += 1
    print(result)


def intersect_in_area(hailstone1: Hailstone, hailstone2: Hailstone) -> bool:
    # check if not parallel
    if hailstone1.a == hailstone2.a and hailstone1.b != hailstone2.b:
        return False
    # check if not on same line
    elif hailstone1.a == hailstone2.a and hailstone1.b == hailstone2.b:
        return True

    # calc intersection
    x = (hailstone2.b - hailstone1.b) / (hailstone1.a - hailstone2.a)
    y = hailstone1.a * x + hailstone1.b
    if LB <= x <= HB and LB <= y <= HB \
            and not_in_past(hailstone1, hailstone2, x, y):
        return True
    return False


def not_in_past(hailstone1: Hailstone, hailstone2: Hailstone, x, y) -> bool:
    if hailstone1.vx > 0:
        if not x >= hailstone1.x:
            return False
    elif hailstone1.vx < 0:
        if not x <= hailstone1.x:
            return False
    else:
        if hailstone1.vy > 0:
            if not y >= hailstone1.y:
                return False
        elif hailstone1.vy < 0:
            if not y <= hailstone1.y:
                return False
        else:
            raise ValueError('Hailstone has no velocity')
    if hailstone2.vx > 0:
        if not x >= hailstone2.x:
            return False
    elif hailstone2.vx < 0:
        if not x <= hailstone2.x:
            return False
    else:
        if hailstone2.vy > 0:
            if not y >= hailstone2.y:
                return False
        elif hailstone2.vy < 0:
            if not y <= hailstone2.y:
                return False
        else:
            raise ValueError('Hailstone has no velocity')
    return True


if __name__ == '__main__':
    main('input.txt')
