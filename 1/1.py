import re


def main(filename):
    file = open(filename, 'r')
    solution = 0
    for line in file:
        regex = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))').findall(line)
        n1 = string_to_int(regex[0])
        n2 = string_to_int(regex[-1])
        solution += (n1 * 10 + n2)
        # print(line, n1, n2, n1 * 10 + n2, solution)

    print(solution)
    file.close()


def string_to_int(number):
    if number == "one":
        return 1
    elif number == "two":
        return 2
    elif number == "three":
        return 3
    elif number == "four":
        return 4
    elif number == "five":
        return 5
    elif number == "six":
        return 6
    elif number == "seven":
        return 7
    elif number == "eight":
        return 8
    elif number == "nine":
        return 9
    else:
        return int(number)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # main('./test.txt')
    main('./input.txt')
    # main('./test2.txt')
