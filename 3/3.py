import re
import time


def main(filename):
    file = open(filename, 'r')
    solution = 0
    matrix = []

    for line in file:
        matrix.append(list(line.strip()))

    for index, line in enumerate(matrix):
        # for ch in line:
        #    if ch not in ("#", "&", "+", "$", "*", ".", "%", "@", "=", "-", "/") and not ch.isdigit():
        #        print(ch)

        line_str = ""
        line_str = line_str.join(line)
        regex = re.finditer(r'((?<=.)*(\d+)(?=.*))', line_str)
        for r in regex:
            s = r.start() - 1
            e = r.end() + 1
            is_part = False
            for x in range(index - 1, index + 2):
                for y in range(s, e):
                    if 0 <= x < len(matrix) and 0 <= y < len(line):
                        if matrix[x][y] in ("#", "&", "+", "$", "*", "%", "@", "=", "-", "/"):
                            is_part = True
                            break
                else:
                    continue
                break
            if is_part:
                solution += int(r.group(0))

    print(solution)

    file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start = time.time()

    # main('./test.txt')
    main('./input.txt')
    # main('./test2.txt')

    print("Process time:", (time.time() - start))
