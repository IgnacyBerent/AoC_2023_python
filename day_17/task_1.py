from collections import defaultdict
from queue import PriorityQueue

import numpy as np

UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)

possible_turns = {
    UP: (RIGHT, LEFT),
    DOWN: (LEFT, RIGHT),
    LEFT: (UP, DOWN),
    RIGHT: (DOWN, UP)
}


def main():
    with open('input.txt', 'r') as f:
        data_map = [
            list([int(x) for x in row])
            for row
            in f.read().splitlines()
        ]
    start = (0, 0)
    end = (len(data_map) - 1, len(data_map[0]) - 1)

    # using dijkstra algorithm

    # setting inf distance value for all nodes
    dist = defaultdict(lambda: defaultdict(lambda: np.inf))
    dist[start][RIGHT] = 0
    dist[start][DOWN] = 0

    pq = PriorityQueue()
    pq.put((0, start, RIGHT))
    pq.put((0, start, DOWN))

    while not pq.empty():
        heat_loss, position, direction = pq.get()

        # skip if already found a better path
        if heat_loss > dist[position][direction]:
            continue

        y, x = position
        for _ in range(3):  # can go straight for 3 steps
            y += direction[0]
            x += direction[1]

            # check if we went out of bounds
            if y < 0 or y >= len(data_map) or x < 0 or x >= len(data_map[0]):
                break

            heat_loss += data_map[y][x]
            for new_direction in possible_turns[direction]:
                # update if found a better path
                if heat_loss < dist[(y, x)][new_direction]:
                    dist[(y, x)][new_direction] = heat_loss
                    pq.put((heat_loss, (y, x), new_direction))

    print(min(dist[end].values()))


if __name__ == '__main__':
    main()
