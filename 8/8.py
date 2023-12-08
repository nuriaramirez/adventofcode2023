import re
import time


def main(filename):
    file = open(filename, 'r')

    instructions = list(file.readline().strip())
    nodes = dict()

    file.readline()
    for line in file:
        regex = re.search(r'([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)', line)
        nodes[regex[1]] = (regex[2], regex[3])

    steps = 0
    current_instructions = instructions.copy()
    current_node = "AAA"
    while len(current_instructions) > 0:
        current_instruction = current_instructions.pop(0)
        # print(current_node, current_instruction)

        if current_instruction == "L":
            current_node = nodes[current_node][0]
        else:
            current_node = nodes[current_node][1]
        steps += 1

        if current_node == "ZZZ":
            break

        if len(current_instructions) == 0:
            current_instructions = instructions.copy()

    print(steps)

    file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start = time.time()

    # main('./test.txt')
    main('./input.txt')

    print("Process time:", (time.time() - start))
