import time

import numpy as np


def main(filename):
    file = open(filename, 'r')
    solution = 0
    matrix = []

    for line in file:
        matrix.append(list(line.strip()))

    gears = np.argwhere(np.array(matrix) == "*")

    for gear_x, gear_y in gears:
        gears_numbers = []
        for x in range(gear_x - 1, gear_x + 2):
            for y in range(gear_y - 1, gear_y + 2):
                if 0 <= x < len(matrix) and 0 <= y < len(matrix[x]):
                    if matrix[x][y].isdigit():
                        min_number_y = y
                        max_number_y = y
                        number_y = y
                        number = ""
                        while number_y >= 0 and matrix[x][number_y].isdigit():
                            number = matrix[x][number_y] + number
                            min_number_y = number_y
                            number_y = number_y - 1
                        number_y = y + 1
                        while number_y < len(matrix[x]) and matrix[x][number_y].isdigit():
                            number = number + matrix[x][number_y]
                            max_number_y = number_y
                            number_y = number_y + 1

                        gears_numbers.append([min_number_y, max_number_y, number])
        unique_gears_numbers = np.unique(np.array(gears_numbers), axis=0)
        if len(unique_gears_numbers) == 2:
            solution += int(unique_gears_numbers[0][2]) * int(unique_gears_numbers[1][2])

    print(solution)

    file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start = time.time()

    # main('./test.txt')
    main('./input.txt')
    # main('./test2.txt')

    print("Process time:", (time.time() - start))
