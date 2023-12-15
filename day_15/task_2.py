from functools import cache


def main():
    with open('input.txt', 'r') as file:
        codes = file.readlines()[0].strip().split(',')
    boxes = [Box(i) for i in range(1, 257)]
    for code in codes:
        box_number = determine_box(code)
        if '=' in code:
            boxes[box_number].add_replace_lens(code.split('=')[0], int(code.split('=')[1]))
        elif '-' in code:
            boxes[box_number].delete_len(code.split('-')[0])
    result = sum([box.calculate_focusing_power() for box in boxes])
    print(result)


@cache
def determine_box(code: str) -> int:
    value = 0
    for char in code:
        if char.isalpha():
            value += ord(char)
            value *= 17
            value %= 256
    return value


class Box:
    def __init__(self, number: int):
        self.number = number
        self.lenses = {}

    def add_replace_lens(self, lens: str, force: int):
        self.lenses[lens] = force

    def delete_len(self, lens: str):
        if lens in self.lenses:
            del self.lenses[lens]

    def calculate_focusing_power(self) -> int:
        power = 0
        for i, force in enumerate(self.lenses.values()):
            power += (i+1) * force * self.number
        return power


if __name__ == '__main__':
    main()
