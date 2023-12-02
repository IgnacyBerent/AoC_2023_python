def main():
    with open("input.txt") as file:
        lines = file.readlines()
        all_numbers = list(map(find_numbers, lines))
        print(sum(all_numbers))


def find_numbers(line: str) -> int:
    numbers = list(filter(lambda x: x.isdigit(), line))
    if len(numbers) == 1:
        return make_whole_number(numbers[0], numbers[0])
    else:
        return make_whole_number(numbers[0], numbers[-1])


def make_whole_number(x: int, y: int) -> int:
    return int(str(x) + str(y))


if __name__ == "__main__":
    main()
