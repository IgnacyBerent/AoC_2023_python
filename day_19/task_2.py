from functools import reduce
from bisect import bisect_left, bisect_right

workflows = {}

def compare(
        a: list[tuple[int, int]],
        symbol: str,
        b: int
) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    valid = []
    invalid = []

    a.sort()  # sortujemy listę sekcji

    for section in a:
        if symbol == '>':
            # używamy wyszukiwania binarnego do znalezienia sekcji, które są większe od b
            index = bisect_right(a, (b, b))
            valid.extend(a[index:])
            invalid.extend(a[:index])
        elif symbol == '<':
            # używamy wyszukiwania binarnego do znalezienia sekcji, które są mniejsze od b
            index = bisect_left(a, (b, b))
            valid.extend(a[:index])
            invalid.extend(a[index:])
        elif symbol == '=':
            # używamy wyszukiwania binarnego do znalezienia sekcji, które są równe b
            index_left = bisect_left(a, (b, b))
            index_right = bisect_right(a, (b, b))
            valid.extend(a[index_left:index_right])
            invalid.extend(a[:index_left] + a[index_right:])

    return valid, invalid


def main():
    global workflows
    with open('example.txt', 'r') as file:
        lines = file.readlines()

    accepted = 0

    second_group = False
    for line in lines:
        if line == '\n':
            second_group = True
            continue
        if second_group:
            continue
        else:
            name, instructions = line.strip().split('{')
            instructions = instructions[:-1]
            instr = []
            for ins in instructions.split(','):
                try:
                    condition, next_wf = ins.split(':')
                    instr.append((condition, next_wf))
                except ValueError:
                    instr.append((None, ins))
            workflows[name] = instr

    possibilities = {
        'x': [(1, 4000)],
        'm': [(1, 4000)],
        'a': [(1, 4000)],
        's': [(1, 4000)],
    }

    result = calc_possib(possibilities, workflows['in'])
    print(result)


def calc_possib(xmas, instructions):
    global workflows
    total_possibs = 0
    for instr in instructions:
        if instr[0] is not None:
            cat = ''
            symb = ''
            num = ''
            for char in instr[0]:
                if char.isalpha():
                    cat = char
                elif char.isdigit():
                    num += char
                else:
                    symb = char
            valid, unvalid = compare(xmas[cat], symb, int(num))
            xmas[cat] = valid
            if instr[1] == 'A':
                total_possibs += reduce(lambda acc, curr: acc * sum([y-x+1 for x,y in curr]), xmas.values())
            else:
                total_possibs += calc_possib(xmas, workflows[instr[1]])
            xmas[cat] = unvalid
        else:
            if instr[1] == 'A':
                return reduce(lambda acc, curr: acc * sum([y-x+1 for x,y in curr]), xmas.values()) + total_possibs
            elif instr[1] == 'R':
                return total_possibs
            else:
                total_possibs += calc_possib(xmas, workflows[instr[1]])
                return total_possibs


if __name__ == "__main__":
    main()
