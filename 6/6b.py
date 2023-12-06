import math
import time


def main(filename):
    file = open(filename, 'r')

    line = file.readline()
    record = int(line[line.find(":") + 1:].replace(" ", "").strip())

    line = file.readline()
    distance = int(line[line.find(":") + 1:].replace(" ", "").strip())

    delta = pow(pow(record, 2) - 4 * distance, 0.5)

    solution1 = (record * -1 + delta) / -2
    min_valid = math.ceil(solution1)
    if min_valid == solution1:
        min_valid += 1

    solution2 = (record * -1 - delta) / -2
    max_valid = math.floor(solution2)
    if max_valid == solution2:
        max_valid -= 1

    print(max_valid - min_valid + 1)

    file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start = time.time()

    # main('./test.txt')
    main('./input.txt')

    print("Process time:", (time.time() - start))
