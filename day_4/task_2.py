def main():
    with open("input.txt", "r") as file:
        lines = file.readlines()

        list_of_cards = []
        for line in lines:
            card_card_number, scratches = line.strip().split(":")
            _, card_number = card_card_number.strip().split()
            winning_scratch, my_scratch = scratches.strip().split("|")
            winning_scratch = [int(scratch) for scratch in winning_scratch.strip().split()]
            my_scratch = [int(card) for card in my_scratch.strip().split()]
            scratches_tuple = (winning_scratch, my_scratch)
            list_of_cards.append((int(card_number), scratches_tuple))
            cards_dict = {int(card_number): tuple for card_number, tuple in list_of_cards}

        i = 0
        while i < len(list_of_cards):
            card_number, scratches = list_of_cards[i]
            matches = calculate_matches(scratches)
            if matches == 0:
                pass
            else:
                for j in range(1, matches+1):
                    list_of_cards.insert(i+j, (card_number+j, cards_dict[card_number+j]))
            i += 1
        print(len(list_of_cards))


def calculate_matches(scratches: tuple[list, list]) -> int:
    matches = 0
    for scratch in scratches[0]:
        if scratch in scratches[1]:
            matches += 1
    return matches


if __name__ == "__main__":
    main()