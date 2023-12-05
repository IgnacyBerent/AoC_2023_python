import time

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

    total_seeds = 1_399_051_681
    start_time = time.time()
    for seed in range(total_seeds):
        # for progress calculation
        current_time = time.time()
        if current_time - start_time >= 60:  # check every 60s
            progress = seed / total_seeds * 100
            print(f'Progress: {progress} %')
            start_time = current_time
        loc = seed
        for category in categories:
            seed = reverse_translate(category, seed)
        if seed_in_range(seed, seeds_ranges):
            print(f'Closest location is: {loc}')
            break


def gen_lowest_location(hum_to_loc_map: list[list[int]]):
    for i in range(len(hum_to_loc_map)):
        final_loc = hum_to_loc_map[i][0]
        final_lon_range = hum_to_loc_map[i][2]
        for i in range(final_loc, final_loc + final_lon_range):
            yield i


def reverse_translate(cat_map: list[list[int]], number: int) -> int:
    for dest_start, source_start, range_ in cat_map:
        if dest_start <= number <= dest_start + range_:
            return source_start + (number - dest_start)
    return number


def give_seeds_ranges(seeds_map: list[int]) -> list[list[int]]:
    seeds_ranges = []
    for i in range(0, len(seeds_map), 2):
        seeds_ranges.append([seeds_map[i], seeds_map[i] + seeds_map[i + 1]])
    return seeds_ranges


def seed_in_range(loc: int, seed_ranges: list[list[int]]) -> bool:
    for seed_range in seed_ranges:
        if seed_range[0] <= loc <= seed_range[1]:
            return True
    return False


if __name__ == '__main__':
    main()
