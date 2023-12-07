with open('input07.txt') as f:
    lines = f.read().strip().split("\n")

hands = {hand: int(bid) for hand, bid in [line.split() for line in lines]}


def compare_same(zipped_hands, strengths):
    # Compare hands that are the same type
    for s1, s2 in zipped_hands:
        if strengths[s1] > strengths[s2]:
            return False
        if strengths[s1] < strengths[s2]:
            return True
    return None


def sort_cards(strengths, part2):
    ordered_hands = []
    for hand in hands.keys():
        amounts = {card: hand.count(card) for card in strengths.keys()}
        sorted_amounts = {k: v for k, v in sorted(amounts.items(), key=lambda item: item[1], reverse=True)}
        if part2:
            f_key, s_key = list(sorted_amounts.keys())[:2]
            if f_key != "J":
                sorted_amounts[f_key] += amounts["J"]
            else:
                sorted_amounts[s_key] += amounts["J"]
            sorted_amounts.pop("J")

        sorted_amounts = list(sorted_amounts.values())
        # Assign Hand type: Five of a kind, Four of a kind, Full House, ...
        if sorted_amounts[0] == 5:
            hand_type = 7
        elif sorted_amounts[0] == 4:
            hand_type = 6
        elif sorted_amounts[0:2] == [3,  2]:
            hand_type = 5
        elif sorted_amounts[0] == 3:
            hand_type = 4
        elif sorted_amounts[0:2] == [2, 2]:
            hand_type = 3
        elif sorted_amounts[0] == 2:
            hand_type = 2
        else:
            hand_type = 1

        # Find index i at which current hand should be
        i = 0
        while True:
            if i >= len(ordered_hands):
                break
            h, ht = ordered_hands[i]

            if hand_type < ht:
                break
            if hand_type > ht:
                i += 1
            if hand_type == ht:
                smaller = compare_same(zip(hand, h), strengths)
                if smaller:
                    break
                else:
                    i += 1
        ordered_hands.insert(i, (hand, hand_type))
    return ordered_hands


def calculations(strengths, part2):
    out = 0
    for i, (hand, _) in enumerate(sort_cards(strengths, part2=part2)):
        out += (i+1) * hands[hand]
    print(f"Part {2 if part2 else 1}: {out}")


calculations(strengths={"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9,
                        "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}, part2=False)

calculations(strengths={"A": 13, "K": 12, "Q": 11, "T": 10,
                        "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "J": 1}, part2=True)
