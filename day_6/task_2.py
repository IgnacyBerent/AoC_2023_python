def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        time = list(lines[0].strip().split(':')[1].split())
        distance = list(lines[1].strip().split(':')[1].split())
        time = int(''.join(time))
        distance = int(''.join(distance))
        result = calc_wins(time, distance)
        print(result)


def calc_distance(hold_time: int, time: int) -> int:
    if time == hold_time:
        return 0
    time -= hold_time
    return hold_time * time


def calc_wins(t: int, d: int) -> int:
    wins = 0
    for h in range(t):
        if calc_distance(h, t) > d:
            wins += 1
    return wins


if __name__ == '__main__':
    main()
