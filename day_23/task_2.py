def main(file: str):
    with open(file, 'r') as f:
        forest = [list(line.strip()) for line in f.readlines()]

    start = (0, 1)
    end = (len(forest) - 1, len(forest[0]) - 2)
    nodes = [start, end]
    # find nodes
    for y in range(len(forest)):
        for x in range(len(forest[0])):
            if forest[y][x] == '.':
                poss = 0
                for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    neigh_y = y + d[0]
                    neigh_x = x + d[1]
                    # if not out of bounds and not a wall
                    if (0 <= neigh_y < len(forest) and 0 <= neigh_x < len(forest[0])
                            and forest[neigh_y][neigh_x] != '#'):
                        poss += 1
                if poss >= 3:
                    nodes.append((y, x))

    graph = {node: {} for node in nodes}

    for sy, sx in nodes:
        stack = [(0, sy, sx)]
        visited = {(sy, sx)}
        while stack:
            n, y, x = stack.pop()

            if n != 0 and (y, x) in nodes:
                graph[(sy, sx)][(y, x)] = n
                continue

            for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_y = y + d[0]
                new_x = x + d[1]
                if (0 <= new_y < len(forest) and 0 <= new_x < len(forest[0])
                        and forest[new_y][new_x] != '#'
                        and (new_y, new_x) not in visited):
                    stack.append((n + 1, new_y, new_x))
                    visited.add((new_y, new_x))

    seen = set()

    def find_longest_path(pt):
        if pt == end:
            return 0

        path = float('-inf')

        seen.add(pt)
        for next_node in graph[pt]:
            if next_node not in seen:
                path = max(path, graph[pt][next_node] + find_longest_path(next_node))
        seen.remove(pt)

        return path

    print(find_longest_path(start))


if __name__ == '__main__':
    main('input.txt')
