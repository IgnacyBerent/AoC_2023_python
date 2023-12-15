from collections import Counter


card_strengths = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, '9': 9,
                  '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}


class Hand:
    def __init__(self, cards, bid):
        """
        Creates Card object
        :param cards: cards in hand
        :param bid: bid related to hand
        """
        self.bid = bid
        self._cards = list(cards)
        self.strength = self.calculate_strength()
        self.type = self.determine_type()

    def calculate_strength(self) -> int:
        """
        Calculates strength of hand
        """
        strenght = 0
        for i, card in enumerate(self._cards):
            strenght += card_strengths[card] * (14 ** (4 - i))
        return strenght

    def determine_type(self) -> int:
        """
        Determines type of hand
        :return: type of hand
        """

        if 'J' in self._cards:
            jokers = self._cards.count('J')
            cards_collection = Counter(self._cards)

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
        else:
            cards_collection = Counter(self._cards)
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

    def __gt__(self, other):
        """
        Compares two cards
        :param other: other Card
        :return: firstly compares types if equal then strengths
        """
        if isinstance(other, Hand):
            if self.type == other.type:
                return self.strength > other.strength
            else:
                return self.type > other.type
        return NotImplemented


def main():
    hands = []
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            hand, bid = line.split()
            hands.append(Hand(hand, int(bid)))

    hands.sort()
    total_winnings = 0
    for i, card in enumerate(hands):
        total_winnings += (i + 1) * card.bid
    print(total_winnings)


if __name__ == '__main__':
    main()
