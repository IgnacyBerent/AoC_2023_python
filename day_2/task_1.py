def find_possible_games():
    with open("input.txt") as file:
        lines = file.readlines()
        possible_games = []
        for line in lines:
            game, sets_line = line.split(':')
            _, game_number = game.split()
            sets_list = sets_line.split(';')
            for set in sets_list:
                possible = True
                greens = 0
                reds = 0
                blues = 0
                dices = set.split(',')
                for dice in dices:
                    number, color = dice.split()
                    if color == 'green':
                        greens = int(number)
                    elif color == 'red':
                        reds = int(number)
                    elif color == 'blue':
                        blues = int(number)
                if reds > 12 or greens > 13 or blues > 14:
                    possible = False
                    break
            if possible:
                possible_games.append(int(game_number))
    return possible_games


def main():
    possible_games = find_possible_games()
    print(sum(possible_games))


if __name__ == "__main__":
    main()
