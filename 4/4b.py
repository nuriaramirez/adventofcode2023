import re
import time
from collections import defaultdict


def main(filename):
    file = open(filename, 'r')

    cards = {}
    cards = defaultdict(lambda: 0, cards)

    for line in file:
        card_index = int(re.search(r'Card\s+(\d+):', line)[1])
        cards[card_index] += 1

        line_numbers = line[line.find(":") + 2:].split()

        winning_numbers = line_numbers[:line_numbers.index("|")]
        numbers = line_numbers[line_numbers.index("|") + 1:]

        next_card = card_index + 1
        for number in winning_numbers:
            if number in numbers:
                cards[next_card] += 1 * cards[card_index]
                next_card += 1
        # print(cards)

    print(sum(cards.values()))

    file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start = time.time()

    # main('./test.txt')
    main('./input.txt')
    # main('./test2.txt')

    print("Process time:", (time.time() - start))
