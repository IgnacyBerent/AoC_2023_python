from collections import Counter
from itertools import chain

card_strengths = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9,
                  '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}


def main():
    hand_to_bid = {}
    types_lists = {7: [], 6: [], 5: [], 4: [], 3: [], 2: [], 1: []}
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            hand, bid = line.split()
            hand_to_bid[hand] = int(bid)
            types_lists[determine_type(hand)].append(hand)

    for key, value in types_lists.items():
        types_lists[key] = sorted(value, key=lambda x: calculate_strength(x), reverse=True)

    all_cards_sorted = list(chain.from_iterable(types_lists.values()))
    all_cards_sorted.reverse()
    total_winnings = 0
    for i, hand in enumerate(all_cards_sorted):
        total_winnings += (i + 1) * hand_to_bid[hand]
    print(total_winnings)


def determine_type(cards: str) -> int:
    """
    Determines type of hand
    :param cards: cards in hand
    :return: value of type where 7 is the best and 1 is the worst
    """
    cards = list(cards)
    cards_collection = Counter(cards)
    if len(cards_collection) == 1:  # Five of a kind
        return 7
    elif len(cards_collection) == 2:  # Four of a kind or Full house
        if 4 in cards_collection.values():  # Four of a kind
            return 6
        else:  # Full house
            return 5
    elif len(cards_collection) == 3:  # Three of a kind or Two pairs
        if 3 in cards_collection.values():  # Three of a kind
            return 4
        else:  # Two pairs
            return 3
    elif len(cards_collection) == 4:  # One pair
        return 2
    else:  # High card
        return 1


def calculate_strength(cards: str) -> int:
    """
    Calculates strength of hand treating cards like number system with base 14
    :param cards: cards in hand
    :return: strength of hand
    """
    strength = 0
    for i, card in enumerate(cards):
        strength += card_strengths[card] * (14 ** (4 - i))
    return strength


if __name__ == '__main__':
    main()
