nums_word = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def main():
    with open("input.txt") as file:
        lines = file.readlines()
        all_numbers = list(map(find_numbers, lines))
        print(sum(all_numbers))


def find_numbers(line: str) -> int:
    numbers = []
    for i, char in enumerate(line):
        if char.isdigit():
            numbers.append(int(char))
        elif char.isalpha():
            word = ''
            for j in range(6):
                try:
                    line[i + j]
                except IndexError:
                    break
                if line[i + j].isalpha():
                    word += line[i + j]
                else:
                    break
                if word in nums_word:
                    numbers.append(nums_word[word])
                    break
    return make_whole_number(numbers)


def make_whole_number(numbers: list) -> int:
    if len(numbers) == 1:
        return int(str(numbers[0]) + str(numbers[0]))
    else:
        return int(str(numbers[0]) + str(numbers[-1]))


if __name__ == "__main__":
    main()
