def get_field_config(file):
    data = file.replace(' ', '').replace('\n', '')
    array = [[0 for i in range(10)] for j in range(10)]
    letter = 'W'
    for i in range(0, len(data) - 2, 2):
        if int(data[i]) != 0:
            array[int(data[i + 1])][int(data[i])] = letter
        else:
            letter = 'B'
            continue
    for i in [0, 9]:
        for j in range(10):
            array[i][j] = 'WB'
    for i in range(10):
        for j in [0, 9]:
            array[i][j] = 'WB'
    return array


def main():
    with open('in.txt') as file:
        field = get_field_config(file.read())
    for l in field:
        print(l)


if __name__ == '__main__':
    main()
