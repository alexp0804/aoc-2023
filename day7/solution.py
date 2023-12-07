
import sys, re
from enum import IntEnum
from functools import cmp_to_key

if len(sys.argv) != 2:
    print(f'Usage: python3 solution.py input_file_name')
    exit(1)

input_file_name = sys.argv[1]

with open(input_file_name) as f:
    cards = [x.split() for x in f.readlines()]

hand_to_bid = {}
all_hands = []
for hand, bid in cards:
    hand_to_bid[hand] = int(bid)
    all_hands.append(hand)

HandType = IntEnum('HandType', ['HIGH_CARD', 'ONE_PAIR', 'TWO_PAIR', 'THREE_OF_A_KIND', \
                                'FULL_HOUSE', 'FOUR_OF_A_KIND', 'FIVE_OF_A_KIND'])

labels = None
labels_part_1 = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
labels_part_2 = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

def classify_type_part_1(hand) -> int:
    label_counts = {label:0 for label in labels_part_1}

    for label in list(hand):
        label_counts[label] += 1
    
    counts = list(label_counts.values())

    one_counts, two_counts, three_counts, four_counts, five_counts \
          = [sum(1 for count in counts if count == i) for i in range(1, 6)]

    if five_counts > 0:
        return HandType.FIVE_OF_A_KIND

    if four_counts == 1 and one_counts == 1:
        return HandType.FOUR_OF_A_KIND

    if three_counts == 1 and two_counts == 1:
        return HandType.FULL_HOUSE

    if three_counts == 1 and one_counts == 2:
        return HandType.THREE_OF_A_KIND

    if two_counts == 2 and one_counts == 1:
        return HandType.TWO_PAIR

    if two_counts == 1 and one_counts == 3:
        return HandType.ONE_PAIR 

    return HandType.HIGH_CARD 

def classify_type_part_2(hand) -> int:
    if 'J' not in set(hand):
        return classify_type_part_1(hand)

    labels_no_joker = set(labels_part_1).difference({'J'})

    og_hand = hand
    best_type = HandType.HIGH_CARD

    for label in labels_no_joker:
        hand = re.sub('J', label, og_hand)
        best_type = max(best_type, classify_type_part_1(hand))
    
    return best_type

def compare(hand_1, hand_2):
    for card_1, card_2 in zip(list(hand_1), list(hand_2)):

        card_1_val = labels.index(card_1)
        card_2_val = labels.index(card_2)

        if card_1_val < card_2_val:
            return -1

        elif card_1_val > card_2_val:
            return 1

    return 0

def calculate_winnings(type_classifier, _labels):
    global labels
    labels = _labels

    hands_by_type = [[] for _ in range(len(HandType))]

    for hand in all_hands:
        hand_type = type_classifier(hand)
        hands_by_type[hand_type - 1].append(hand)

    for hands in hands_by_type:
        hands.sort(key=cmp_to_key(compare))

    winnings = 0
    rank = len(all_hands)

    for hands in reversed(hands_by_type):
        for hand in reversed(hands):
            winnings += rank * hand_to_bid[hand]
            rank -= 1
    
    return winnings

ans_part_1 = calculate_winnings(classify_type_part_1, labels_part_1)
ans_part_2 = calculate_winnings(classify_type_part_2, labels_part_2)

print(f'The answer\n\tpart 1:{ans_part_1}\n\tpart 2:{ans_part_2}')