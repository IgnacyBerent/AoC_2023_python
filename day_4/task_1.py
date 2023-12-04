def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        total_points = 0
        for line in lines:
            _, cards = line.strip().split(":")
            winning_cards, my_cards = cards.strip().split("|")
            winning_cards = [int(card) for card in winning_cards.strip().split()]
            my_cards = [int(card) for card in my_cards.strip().split()]
            points = 0
            for card in my_cards:
                if card in winning_cards:
                    if points == 0:
                        points = 1
                    else:
                        points *= 2
            total_points += points
        print(total_points)


if __name__ == "__main__":
    main()
