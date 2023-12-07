from collections import Counter
from itertools import chain
from task_1 import determine_type

card_strengths = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, '9': 9,
                  '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}


def main():
    # instead make dictionary with value as a key and list of hands as a value
    hand_to_bid = {}
    types_lists = {7: [], 6: [], 5: [], 4: [], 3: [], 2: [], 1: []}
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            hand, bid = line.split()
            hand_to_bid[hand] = int(bid)
            if 'J' in hand:
                type = determine_type_j(hand)
            else:
                type = determine_type(hand)
            types_lists[type].append(hand)

    for key, value in types_lists.items():
        types_lists[key] = sorted(value, key=lambda x: calculate_strenght(x), reverse=True)

    all_cards_sorted = list(chain.from_iterable(types_lists.values()))
    all_cards_sorted.reverse()
    total_winnings = 0
    for i, hand in enumerate(all_cards_sorted):
        total_winnings += (i + 1) * hand_to_bid[hand]
    print(total_winnings)


def determine_type_j(cards: str) -> int:
    """
    determine type of hand with jokers
    :param cards: card with at least one joker
    :return: type of hand
    """
    cards = list(cards)
    jokers = cards.count('J')
    cards_collection = Counter(cards)

    if len(cards_collection) == 1:  # Five of a kind
        return 7

    if cards_collection.most_common(1)[0][0] != 'J':
        common_w_j = cards_collection.most_common(1)[0][1] + jokers
    else:
        common_w_j = cards_collection.most_common(2)[1][1] + jokers

    if common_w_j == 5:  # Five of a kind
        return 7
    elif common_w_j == 4:  # Four of a kind
        return 6
    elif common_w_j == 3:  # Three of a kind or Full house
        if len(cards_collection) == 3:  # Full house
            return 5
        else:  # Three of a kind
            return 4
    else:  # One pair
        return 2


def calculate_strenght(cards: str) -> int:
    """
    treats cards like number system with base 14
    """
    strenght = 0
    for i, card in enumerate(cards):
        strenght += card_strengths[card] * (14 ** (4 - i))
    return strenght


if __name__ == '__main__':
    main()
