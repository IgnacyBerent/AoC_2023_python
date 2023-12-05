def main():
    categories = []
    seeds = []

    with open('input.txt', 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if line == lines[0]:
                seeds = list(map(int, line.split(':')[1].strip().split()))
                continue
            if i == 1:
                continue
            if line[0].isalpha():
                new_category = []
            elif not line.strip():
                categories.append(new_category)
            else:
                new_category.append(list(map(int, line.strip().split())))
        categories.append(new_category)

    for category in categories:
        seeds = list(map(lambda x: translate(category, x), seeds))

    print(min(seeds))


def translate(cat_map: list[list[int]], number: int) -> int:
    for dest_start, source_start, range_ in cat_map:
        if source_start <= number <= source_start + range_:
            return dest_start + (number - source_start)
    return number


if __name__ == '__main__':
    main()
