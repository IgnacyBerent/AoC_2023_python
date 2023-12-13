from itertools import groupby


def main():
    with open('input.txt', 'r') as file:
        lines = file.read().splitlines()
    patterns = [list(g) for k, g in groupby(lines, bool) if k]
    result = sum(find_reflections(pattern) for pattern in patterns)
    print(result)


def find_reflections(p: list[str]) -> int:
    vertical = p
    horizontal = [list(i) for i in zip(*p[::-1])]

    for pattern in (vertical, horizontal):
        length = len(pattern)
        for center in range(1, length):
            checks = min(center, length - center)
            if sum(diffs(pattern[center - 1 - j], pattern[center + j]) for j in range(checks)) == 1:
                return center if pattern == horizontal else center * 100


def diffs(str1, str2) -> int:
    return sum(a != b for a, b in zip(str1, str2))


if __name__ == '__main__':
    main()
