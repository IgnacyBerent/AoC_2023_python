from collections import defaultdict, deque


def main(file: str):
    components_map = defaultdict(set)

    with open(file) as f:
        data = f.readlines()
    for line in data:
        l, r = line.strip().split(': ')
        r = r.split(' ')
        for comp in r:
            components_map[l].add(comp)
            components_map[comp].add(l)

    group_1 = 1
    group_2 = 0

    first_comp = list(components_map.keys())[0]

    for i, component in enumerate(list(components_map.keys())[1:]):
        print(i)
        connections = 0
        used_components = {first_comp}
        # finds shortest path for considered component
        # for each of starting component without repeating used components
        for s_component in components_map[first_comp]:
            if s_component == component:
                connections += 1
                continue
            q = deque()
            q.append((s_component, [s_component], 0))
            found = False
            while q and not found and connections < 4:
                comp, path, steps = q.popleft()
                for c in components_map[comp]:
                    if c not in path and c not in used_components:
                        if component == c:
                            connections += 1
                            used_components.update(path)
                            found = True
                            break
                        elif steps < 20:
                            q.append([c, path + [c], steps + 1])
        # If it finds more than 3 unique ways to get to given component then it is in group 1
        if connections >= 4:
            group_1 += 1
        else:
            group_2 += 1

    print(group_1 * group_2)


if __name__ == '__main__':
    main('input.txt')
