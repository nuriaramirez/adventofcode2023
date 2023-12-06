import math
import time
from functools import reduce


def main(filename):
    file = open(filename, 'r')

    line = file.readline()
    times = [int(x) for x in line[line.find(":") + 1:].split()]

    line = file.readline()
    distances = [int(x) for x in line[line.find(":") + 1:].split()]

    solutions = [0] * len(times)

    for index, record in enumerate(times):
        delta = pow(pow(record, 2) - 4 * distances[index], 0.5)

        solution1 = (record * -1 + delta) / -2
        min_valid = math.ceil(solution1)
        if min_valid == solution1:
            min_valid += 1

        solution2 = (record * -1 - delta) / -2
        max_valid = math.floor(solution2)
        if max_valid == solution2:
            max_valid -= 1

        solutions[index] = max_valid - min_valid + 1

    print(solutions)
    print(reduce((lambda x, y: x * y), solutions))

    file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start = time.time()

    main('./test.txt')
    # main('./input.txt')

    print("Process time:", (time.time() - start))
