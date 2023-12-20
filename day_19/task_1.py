def compare(a: int, symbol: str, b: int):
    if symbol == '>':
        return a > b
    elif symbol == '<':
        return a < b
    elif symbol == '=':
        return a == b


def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    accepted = 0

    workflows = {}
    parts = []
    second_group = False
    for line in lines:
        if line == '\n':
            second_group = True
            continue
        if second_group:
            part_dict = {}
            for part in line.strip()[1:-1].split(','):
                key, value = part.split('=')
                part_dict[key] = int(value)
            parts.append(part_dict)
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

    for part in parts:
        instructions = workflows['in']
        i = 0
        while True:
            instr = instructions[i]
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
                if compare(part[cat], symb, int(num)):
                    if instr[1] == 'A':
                        accepted += sum([x for x in part.values()])
                        break
                    elif instr[1] == 'R':
                        break
                    else:
                        instructions = workflows[instr[1]]
                        i = 0
                else:
                    i += 1
            else:
                if instr[1] == 'A':
                    accepted += sum([x for x in part.values()])
                    break
                elif instr[1] == 'R':
                    break
                else:
                    instructions = workflows[instr[1]]
                    i = 0

    print(accepted)


if __name__ == "__main__":
    main()
