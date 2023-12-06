import time


def main(filename):
    file = open(filename, 'r')

    min_location = -1

    seeds = []

    line = file.readline()
    seeds.extend([int(x) for x in line[line.find(":") + 1:].strip().split(" ")])

    file.readline()
    maps = [read_map(file), read_map(file), read_map(file), read_map(file), read_map(file), read_map(file),
            read_map(file)]

    for seed in seeds:
        # print("Seed", seed)
        number = seed
        for m in maps:
            # print("Map", m)
            for r in m:
                # print("Range", r)
                if r[1] <= number < (r[1] + r[2]):
                    number = r[0] + (number - r[1])
                    break

        # print("Location", number)
        if min_location == -1:
            min_location = number
        else:
            min_location = min(min_location, number)

    print(min_location)

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
