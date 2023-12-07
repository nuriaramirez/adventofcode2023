import time
from collections import defaultdict

CARD_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def main(filename):
    file = open(filename, 'r')

    solutions = []

    for line in file:
        hand, bid = line.strip().split(" ")

        hand_type = defaultdict(lambda: 0)
        for card in hand:
            hand_type[card] += 1

        t = 0
        # Five of a kind
        if 5 in hand_type.values():
            t = 1
        # Four of a kind
        elif 4 in hand_type.values():
            t = 2
        elif 3 in hand_type.values():
            # Full house
            if 2 in hand_type.values():
                t = 3
            # Three of a kind
            else:
                t = 4
        elif 2 in hand_type.values():
            # Two pair
            if len(hand_type.values()) == 3:
                t = 5
            # One pair
            else:
                t = 6
        # High card
        else:
            t = 7

        values = [CARD_VALUES.index(x) for x in list(hand)]
        solutions.append([t, hand, int(bid), values])

    solution = 0
    i = 1
    for item in sorted(solutions, key=lambda x: (-x[0], x[3][0], x[3][1], x[3][2], x[3][3], x[3][4])):
        # print(i, item)
        solution += i * item[2]
        i += 1

    print(solution)

    file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start = time.time()

    # main('./test.txt')
    main('./input.txt')

    print("Process time:", (time.time() - start))
