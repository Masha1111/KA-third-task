def get_field_config(file):
    data = file.replace(' ', '').replace('\n', '')
    array = [[0 for i in range(8)] for j in range(8)]
    letter = 'W'
    for i in range(0, len(data) - 2, 2):
        if int(data[i]) != 0:
            array[int(data[i + 1]) - 1][int(data[i]) - 1] = letter
        else:
            letter = 'B'
            continue
    return array


def main():
    with open('in.txt') as file:
        field = get_field_config(file.read())
    for l in field:
        print(l)


if __name__ == '__main__':
    main()
