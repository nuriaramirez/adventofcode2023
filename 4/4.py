import time


def main(filename):
    file = open(filename, 'r')
    solution = 0

    for line in file:
        line_numbers = line[line.find(":") + 2:].split()

        winning_numbers = line_numbers[:line_numbers.index("|")]
        numbers = line_numbers[line_numbers.index("|") + 1:]

        partial_solution = 0
        for number in winning_numbers:
            if number in numbers:
                partial_solution += 1
        if partial_solution > 0:
            solution += pow(2, partial_solution - 1)

    print(solution)

    file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start = time.time()

    # main('./test.txt')
    main('./input.txt')

    print("Process time:", (time.time() - start))
