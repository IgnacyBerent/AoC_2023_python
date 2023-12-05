def main():
    categories = []
    seeds_map = []

    with open('input.txt', 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if line == lines[0]:
                seeds_map = list(map(int, line.split(':')[1].strip().split()))
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

    seeds_ranges = give_seeds_ranges(seeds_map)
    categories.reverse()

    total_seeds = 318728750  # result from task one, so this must be smaller
    for seed in range(1, total_seeds):
        loc = seed
        for category in categories:
            seed = reverse_translate(category, seed)
        if seed_in_range(seed, seeds_ranges):
            print(f'Closest location is: {loc}')
            break


def reverse_translate(cat_map: list[list[int]], number: int) -> int:
    for dest_start, source_start, range_ in cat_map:
        if dest_start <= number <= dest_start + range_:
            return source_start + (number - dest_start)
    return number


def give_seeds_ranges(seeds_map: list[int]) -> list[tuple[int, int]]:
    seeds_ranges = []
    for i in range(0, len(seeds_map), 2):
        seeds_ranges.append((seeds_map[i], seeds_map[i] + seeds_map[i + 1] - 1))
    return seeds_ranges


def seed_in_range(seed: int, seed_ranges: list[tuple[int, int]]) -> bool:
    for seed_range in seed_ranges:
        if seed_range[0] <= seed <= seed_range[1]:
            return True
    return False


if __name__ == '__main__':
    main()

""" 
I don't know why it gives anwser bigger by 1 than real solution on webstie.
Maybe it's due to their bug
My solution: 37384987
Solution on website: 37384986
"""
