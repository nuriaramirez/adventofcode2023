import re
import time


def main(filename):
    file = open(filename, 'r')
    solution = 0

    for line in file:
        possible = True
        regex = re.match(r'Game (\d*): (.*)', line)
        game_id = int(regex[1])
        sets = regex[2].split(";")
        for s in sets:
            for color in s.split(","):
                color_re = re.match(r'(\d+) (red|green|blue)', color.strip())
                possible = possible and is_possible(int(color_re[1]), color_re[2])
                # print(color, possible)

        if possible:
            solution += game_id

    print(solution)

    file.close()


def is_possible(number, color):
    if color == "red":
        if number <= 12:
            return True
    elif color == "green":
        if number <= 13:
            return True
    elif color == "blue":
        if number <= 14:
            return True
    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start = time.time()

    # main('./test.txt')
    main('./input.txt')

    print("Process time:", (time.time() - start))
