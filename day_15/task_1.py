from functools import cache


def main():
    with open('input.txt', 'r') as file:
        codes = file.readlines()[0].strip().split(',')
    total_sum = 0
    for code in codes:
        total_sum += translate(code)
    print(total_sum)


@cache
def translate(code: str) -> int:
    value = 0
    for char in code:
        value += ord(char)
        value *= 17
        value %= 256
    return value


if __name__ == '__main__':
    main()
