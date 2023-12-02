def main():
    powers = []
    with open("input.txt", 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            _, sets_line = line.split(':')
            sets_list = sets_line.split(';')
            reds = []
            greens = []
            blues = []
            for dice_set in sets_list:
                dices = dice_set.split(',')
                for dice in dices:
                    number, color = dice.split()
                    if color == 'green':
                        greens.append(int(number))
                    elif color == 'red':
                        reds.append(int(number))
                    elif color == 'blue':
                        blues.append(int(number))
            power = max(reds) * max(greens) * max(blues)
            powers.append(power)
    print(sum(powers))


if __name__ == "__main__":
    main()
