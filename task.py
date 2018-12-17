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
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i != 0 and j != 0:
                if (node[0] + i, node[1] + j) not in indexes[char]:
                    if (node[0] + i, node[1] + j) not in indexes[another_char]:
                        possible_places.append((node[0] + i, node[1] + j))
                if (node[0] + i, node[1] + j) in indexes[char]:
                    result.append((node[0] + i, node[1] + j))
    return result, possible_places


def search(letter, another_letter, indexes):
    visited = set()
    if not indexes[letter]:
        return
    queue = [indexes[letter][0]]
    counter = 0
    answer = [[], []]
    while queue:
        current = queue.pop(0)
        if current in visited:
            continue
        visited.add(current)
        neighbours, places = get_neighbours(current, indexes, letter, another_letter)
        if len(places) == 1:
            counter += 1
            answer[another_letter].append(places[0])
        for neighbour in neighbours:
            queue.append(neighbour)
    return answer




def main():
    with open('in.txt') as file:
        field, indexes = get_field_config(file.read())
    answer = []
    for l in range(2):
        answer.append(search(l, (l + 1) % 2, indexes))


if __name__ == '__main__':
    main()
