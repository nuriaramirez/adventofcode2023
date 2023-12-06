import re
import time


def main(filename):
    file = open(filename, 'r')
    solution = 0

    for line in file:
        regex = re.match(r'Game (\d*): (.*)', line)
        min_red = 0
        min_green = 0
        min_blue = 0

        sets = regex[2].split(";")
        for s in sets:
            for color in s.split(","):
                color_re = re.match(r'(\d+) (red|green|blue)', color.strip())
                color_number = int(color_re[1])
                if color_re[2] == "red":
                    if min_red < color_number:
                        min_red = color_number
                elif color_re[2] == "green":
                    if min_green < color_number:
                        min_green = color_number
                elif color_re[2] == "blue":
                    if min_blue < color_number:
                        min_blue = color_number

        solution += min_red * min_green * min_blue

    print(solution)

    file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start = time.time()

    # main('./test.txt')
    main('./input.txt')
    # main('./test2.txt')

    print("Process time:", (time.time() - start))
