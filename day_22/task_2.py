from collections import defaultdict
from collections import deque
from task_1 import fall_bricks, Brick, find_holds

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
        q = deque(j for j in brick.holds if len(j.held_by) == 1)
        falling = set(q)
        falling.add(brick)

        while q:
            j = q.popleft()
            for k in j.holds - falling:
                # if everything that holds k is in falling
                if k.held_by <= falling:
                    q.append(k)
                    falling.add(k)

        result += len(falling) - 1

    print(result)


if __name__ == '__main__':
    main('input.txt')
