def get_field_config(file):
    data = file.replace(' ', '').replace('\n', '')
    array = [[0 for i in range(8)] for j in range(8)]
    letter = 'W'
    indexes = [[], []]
    index = 0
    for i in range(0, len(data) - 2, 2):
        if int(data[i]) != 0:
            array[int(data[i + 1]) - 1][int(data[i]) - 1] = letter
            indexes[index].append((int(data[i + 1]) - 1, int(data[i]) - 1))
        else:
            letter = 'B'
            index = 1
            continue
    return array, indexes


def make_cycles(indexes):
    cycles = [[], []]
    for k in range(2):
        temporary_cycles = []
        pair = indexes[k][0]
        temporary_cycles.append(pair)
        for i in range(pair[0] - 1, pair[0] + 1):
            for j in range(pair[1] - 1, pair[1] + 1):
                if i != -1 and j != -1:
                    if (i, j) in indexes and (i, j) not in temporary_cycles:
                        temporary_cycles.append(i, j)
                        pair = ((i, j))
        if abs(temporary_cycles[0][0] - temporary_cycles[-1][0]) < 3:
            if abs(temporary_cycles[0][1] - temporary_cycles[-1][1]) < 3:
                cycles[k].append(temporary_cycles)
    return cycles



def main():
    with open('in.txt') as file:
        field, indexes = get_field_config(file.read())
    indexes[0].sort()
    indexes[1].sort()
    cycles = make_cycles(indexes)
    print(cycles)


if __name__ == '__main__':
    main()
