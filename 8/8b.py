import re
import time
from functools import reduce


def main(filename):
    file = open(filename, 'r')

    instructions = list(file.readline().strip())
    nodes = dict()
    current_nodes = dict()
    node_steps = []

    file.readline()
    for line in file:
        regex = re.search(r'([A-Z0-9]{3}) = \(([A-Z0-9]{3}), ([A-Z0-9]{3})\)', line)
        nodes[regex[1]] = (regex[2], regex[3])

        if regex[1].endswith("A"):
            current_nodes[regex[1]] = regex[1]

    steps = 0
    current_instructions = instructions.copy()
    while (len(current_nodes) >
           len(node_steps)):
        current_instruction = current_instructions.pop(0)
        # print(current_nodes, current_instruction)

        steps += 1
        for start_node, current_node in current_nodes.items():
            if current_instruction == "L":
                new_node = nodes[current_node][0]
            else:
                new_node = nodes[current_node][1]

            current_nodes[start_node] = new_node

            if new_node.endswith("Z"):
                node_steps.append(steps)

        if len(current_instructions) == 0:
            current_instructions = instructions.copy()

    print(reduce(lambda x, y: int(mcm(x, y)), node_steps))

    file.close()


def mcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def mcm(a, b):
    return (a * b) / mcd(a, b)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start = time.time()

    # main('./test2.txt')
    main('./input.txt')

    print("Process time:", (time.time() - start))
