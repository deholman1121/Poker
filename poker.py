CARDS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
SUITS = ['S', 'C', 'D', 'H']
HANDS = {'High Card': 0, 'Pair': 1, 'Two Pairs': 2, 'Three of a Kind': 3, 'Straight': 4, 'Flush': 5, 'Full House': 6,
         'Four of a Kind': 7, 'Straight Flush': 8, 'Royal Flush': 9}


def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines


def split_hands(lines):
    first_hand = [hand.split()[0:5] for hand in lines]
    second_hand = [hand.split()[5:] for hand in lines]
    return first_hand, second_hand


def split_hand(hand):
    return [card[0] for card in hand], [card[1] for card in hand]


def is_high_straight(cards):
    return set(CARDS[9:]) == set(cards)


def is_straight(cards):
    return any([set(cards) == set(CARDS[i:i + 5]) for i in range(0, len(CARDS) - 4)])


def is_flush(suits):
    return len(set(suits)) == 1


def is_straight_flush(cards, suits):
    return is_straight(cards) and is_flush(suits)


def is_royal_flush(cards, suits):
    return is_high_straight(cards) and is_flush(suits)


def is_four_of_a_kind(cards):
    return [cards.count(i) for i in CARDS[1:]].count(4) == 1


def is_full_house(cards):
    return is_three_of_a_kind(cards) and is_pair(cards)


def is_three_of_a_kind(cards):
    return [cards.count(i) for i in CARDS[1:]].count(3) == 1


def is_two_pair(cards):
    return [cards.count(i) for i in CARDS[1:]].count(2) == 2


def is_pair(cards):
    return [cards.count(i) for i in CARDS[1:]].count(2) == 1


def get_high_pair(cards):
    return max([CARDS[1:].index(pair)+1 for pair in [card for card in CARDS[1:] if cards.count(card) == 2]])


def get_high_three_of_a_kind(cards):
    return max([CARDS[1:].index(pair)+1 for pair in [card for card in CARDS[1:] if cards.count(card) == 3]])


def get_high_four_of_a_kind(cards):
    return max([CARDS[1:].index(pair)+1 for pair in [card for card in CARDS[1:] if cards.count(card) == 4]])


def get_high_card(cards):
    return max([CARDS[1:].index(card)+1 for card in cards])


def get_non_set_high_card(cards):
    return max([CARDS[1:].index(pair)+1 for pair in [card for card in CARDS[1:] if cards.count(card) == 1]])


def get_hand(hand):
    cards, suits = split_hand(hand)
    if is_royal_flush(cards, suits):
        hand_name = 'Royal Flush'
    elif is_straight_flush(cards, suits):
        hand_name = 'Straight Flush'
    elif is_four_of_a_kind(cards):
        hand_name = 'Four of a Kind'
    elif is_full_house(cards):
        hand_name = 'Full House'
    elif is_flush(suits):
        hand_name = 'Flush'
    elif is_straight(cards):
        hand_name = 'Straight'
    elif is_three_of_a_kind(cards):
        hand_name = 'Three of a Kind'
    elif is_two_pair(cards):
        hand_name = 'Two Pairs'
    elif is_pair(cards):
        hand_name = 'Pair'
    else:
        hand_name = 'High Card'

    return hand_name


def compare_hands(hand1, hand2):
    hand1_name = get_hand(hand1)
    hand2_name = get_hand(hand2)

    high_card1 = None
    high_card2 = None
    # print(f'Player 1: {hand1_name}')
    # print(f'Player 2: {hand2_name}')
    if HANDS[hand1_name] > HANDS[hand2_name]:
        return 'Player 1 wins!'
    elif HANDS[hand1_name] < HANDS[hand2_name]:
        return 'Player 2 wins!'
    else:
        cards1, _ = split_hand(hand1)
        cards2, _ = split_hand(hand2)
        if hand1_name in ['High Card', 'Straight', 'Flush', 'Straight Flush', 'Royal Flush']:
            high_card1 = get_high_card(cards1)
            high_card2 = get_high_card(cards2)
            while high_card1 == high_card2 or len(cards1) == 0:
                cards1.remove(CARDS[high_card1])
                cards2.remove(CARDS[high_card2])
                high_card1 = get_high_card(cards1)
                high_card2 = get_high_card(cards2)
        elif hand1_name in ['Pair', 'Two Pairs']:
            high_card1 = get_high_pair(cards1)
            high_card2 = get_high_pair(cards2)
            if hand1_name in ['Two Pairs']:
                if high_card1 == high_card2:
                    cards1.remove(CARDS[high_card1])
                    cards1.remove(CARDS[high_card1])
                    cards2.remove(CARDS[high_card2])
                    cards2.remove(CARDS[high_card2])
                    high_card1 = get_high_pair(cards1)
                    high_card2 = get_high_pair(cards2)
                if high_card1 == high_card2:
                    cards1.remove(CARDS[high_card1])
                    cards1.remove(CARDS[high_card1])
                    cards2.remove(CARDS[high_card2])
                    cards2.remove(CARDS[high_card2])
                    high_card1 = get_high_card(cards1)
                    high_card2 = get_high_card(cards2)
            else:
                if high_card1 == high_card2:
                    cards1.remove(CARDS[high_card1])
                    cards1.remove(CARDS[high_card1])
                    cards2.remove(CARDS[high_card2])
                    cards2.remove(CARDS[high_card2])
                    high_card1 = get_high_card(cards1)
                    high_card2 = get_high_card(cards2)
                    while high_card1 == high_card2 or len(cards1) == 0:
                        cards1.remove(CARDS[high_card1])
                        cards2.remove(CARDS[high_card2])
                        high_card1 = get_high_card(cards1)
                        high_card2 = get_high_card(cards2)

        elif hand1_name in ['Three of a Kind']:
            high_card1 = get_high_three_of_a_kind(cards1)
            high_card2 = get_high_three_of_a_kind(cards2)
            # This shouldn't be true, except considering a case of a shared pile (ex. Texas Hold 'Em)
            if high_card1 == high_card2:
                if high_card1 == high_card2:
                    cards1.remove(CARDS[high_card1])
                    cards1.remove(CARDS[high_card1])
                    cards1.remove(CARDS[high_card1])
                    cards2.remove(CARDS[high_card2])
                    cards2.remove(CARDS[high_card2])
                    cards2.remove(CARDS[high_card2])
                    high_card1 = get_high_card(cards1)
                    high_card2 = get_high_card(cards2)
                    while high_card1 == high_card2 or len(cards1) == 0:
                        cards1.remove(CARDS[high_card1])
                        cards2.remove(CARDS[high_card2])
                        high_card1 = get_high_card(cards1)
                        high_card2 = get_high_card(cards2)
        elif hand1_name in ['Four of a Kind']:
            high_card1 = get_high_four_of_a_kind(cards1)
            high_card2 = get_high_four_of_a_kind(cards2)
            # This shouldn't be true, except considering a case of a shared pile (ex. Texas Hold 'Em)
            if high_card1 == high_card2:
                cards1.remove(high_card1)
                cards1.remove(high_card1)
                cards1.remove(high_card1)
                cards1.remove(high_card1)
                cards2.remove(high_card2)
                cards2.remove(high_card2)
                cards2.remove(high_card2)
                cards2.remove(high_card2)
                high_card1 = get_high_card(cards1)
                high_card2 = get_high_card(cards2)
        # print(f'Player 1 high card: {CARDS[high_card1]}')
        # print(f'Player 2 high card: {CARDS[high_card2]}')

        if high_card1 > high_card2:
            return 'Player 1 wins!'
        elif high_card1 < high_card2:
            return 'Player 2 wins!'
        return 'Tied!'


if __name__ == '__main__':
    hands = read_file('poker.txt')

    player1_hands, player2_hands = split_hands(hands)
    player1_wins = 0
    player2_wins = 0
    ties = 0
    for (player1_hand, player2_hand) in zip(player1_hands, player2_hands):
        # print(f'Player 1 hand: {player1_hand}')
        # print(f'Player 2 hand: {player2_hand}')
        result = compare_hands(player1_hand, player2_hand)
        if 'Player 1 wins!' == result:
            player1_wins += 1
        elif 'Player 2 wins!' == result:
            player2_wins += 1
        elif 'Tied!' == result:
            ties += 1
        # print(f'{result}')

    print(f'Total Number of Player 1 wins: {player1_wins}')
    print(f'Total Number of Player 2 wins: {player2_wins}')
    print(f'Total Number of Ties: {ties}')
