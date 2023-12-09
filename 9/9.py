import time


def main(filename):
    file = open(filename, 'r')

    solutions = []
    numbers = []

    for line in file:
        numbers.append([int(i) for i in line.strip().split(" ")])

        while sum(numbers[-1]) != 0:
            new_list = []
            for index, number in enumerate(numbers[-1]):
                if index+1 < len(numbers[-1]):
                    new_list.append(numbers[-1][index+1]-number)
            numbers.append(new_list)

        numbers.pop()

        last_number = numbers.pop()[-1]
        while len(numbers) > 0:
            last_number += numbers.pop()[-1]
        solutions.append(last_number)

    print(sum(solutions))

    file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start = time.time()

    # main('./test.txt')
    main('./input.txt')

    print("Process time:", (time.time() - start))
