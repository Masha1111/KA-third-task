def get_field_config(file):
    ind = [[], []]
    data = file.replace(' ', '').replace('\n', '')
    array = [[0 for i in range(8)] for j in range(8)]
    letter = 'W'
    for i in range(0, len(data) - 2, 2):
        if int(data[i]) != 0:
            array[int(data[i + 1]) - 1][int(data[i]) - 1] = letter
        else:
            letter = 'B'
            continue
    for i in range(8):
        for j in range(8):
            if array[i][j] == 'B':
                ind[1].append((i, j))
            if array[i][j] == 'W':
                ind[0].append((i, j))
    return array, ind


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def get_neighbours(node, indexes, char, another_char):
    result = []
    possible_places = []
    for tup in directions:
        if (node[0] + tup[0], node[1] + tup[1]) not in indexes[char]:
            if (node[0] + tup[0], node[1] + tup[1]) not in indexes[another_char]:
                possible_places.append((node[0] + tup[0], node[1] + tup[1]))
        if (node[0] + tup[0], node[1] + tup[1]) in indexes[char]:
            result.append((node[0] + tup[0], node[1] + tup[1]))
    return result, possible_places


def search(letter, another_letter, indexes):
    visited = set()
    if not indexes[letter]:
        return None
    queue = [indexes[letter][0]]
    counter = 0
    step = 0
    block = 0
    answer = [[], [], 0, 0]
    while queue:
        current = queue.pop(0)
        block += 1
        visited.add(current)
        neighbours, places = get_neighbours(current, indexes, letter, another_letter)
        possible_points = []
        for place in places:
            if -1 not in place:
                if 8 not in place:
                    possible_points.append(place)
        if len(possible_points) == 1:
            if counter == 0:
                counter += 1
                step = possible_points[0]
            else:
                for neighbour in neighbours:
                    visited.add(neighbour)
        if len(possible_points) > 1:
            step = 0
            counter = 0
            for neighbour in neighbours:
                visited.add(neighbour)
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
        if not queue:
            if step != 0:
                if answer[letter + 2] < block:
                    answer[letter + 2] = block
                    answer[another_letter] = [(step[1] + 1, step[0] + 1)]
                if answer[letter + 2] == block:
                    answer[another_letter].append((step[1] + 1, step[0] + 1))
                step = 0
            for tup in indexes[letter]:
                if tup not in visited:
                    queue.append(tup)
                    counter = 0
                    break
            block = 0
    return answer[another_letter]


def print_result(result):
    with open("out.txt", 'w') as file:
        for i in range(1, -1, -1):
            if result[i]:
                string = ''
                for place in result[i]:
                    string += str(place[0]) + ' ' + str(place[1]) + '  '
                file.write(string)
            else:
                file.write('N\n')


def main():
    with open('in.txt') as file:
        field, indexes = get_field_config(file.read())
    answer = [[], []]
    for l in range(2):
        answer[l] = list(set(search(l, (l + 1) % 2, indexes)))
        answer[l].sort()
    print_result(answer)


if __name__ == '__main__':
    main()
