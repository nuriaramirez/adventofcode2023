import time


def main(filename):
    file = open(filename, 'r')

    seeds = []
    line = file.readline()
    seeds_line = [int(x) for x in line[line.find(":") + 1:].strip().split(" ")]
    for s in range(0, len(seeds_line), 2):
        seeds.append([seeds_line[s], seeds_line[s] + seeds_line[s + 1]])

    file.readline()

    maps = [read_map(file), read_map(file), read_map(file), read_map(file), read_map(file), read_map(file),
            read_map(file)]

    current_list = []
    for seed in seeds:
        current_list = seeds
        next_list = []

        for m in maps:
            while len(current_list) > 0:
                current = current_list.pop()
                found = False
                for r in m:
                    if r[1] <= current[0] < (r[1] + r[2]):
                        found = True
                        if r[1] <= current[1] < (r[1] + r[2]):
                            next_list.append([r[0] + (current[0] - r[1]), r[0] + (current[1] - r[1])])
                        else:
                            next_list.append([r[0] + (current[0] - r[1]), r[0] + r[2]])

                            current_list.append([r[1] + r[2], current[1]])
                        break
                if not found:
                    next_list.append(current)
            current_list = next_list
            next_list = []

    print(min([x[0] for x in current_list]))

    file.close()


def read_map(file):
    map_list = []

    file.readline()
    line = file.readline().strip()

    while line != "":
        map_list.append([int(x) for x in line.split(" ")])
        line = file.readline().strip()

    return map_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start = time.time()

    # main('./test.txt')
    main('./input.txt')

    print("Process time:", (time.time() - start))
