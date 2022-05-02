def snail(snail_map):
    size = len(snail_map)
    print(size)

    result = list()
    lap = 0

    if len(snail_map) == 1 and len(snail_map[0]) == 0:
        return []

    while len(result) != size * size:
        for i in range(size):
            move(snail_map, lap, result, i)

        for i in range(size):
            move(snail_map, i, result, size - lap - 1)

        for i in reversed(range(size)):
            move(snail_map, size - lap - 1, result, i)

        for i in reversed(range(size)):
            move(snail_map, i, result, lap)

        lap += 1

    print('modified map:', snail_map)
    return result


def move(snail_map, lap, result, i):
    if snail_map[lap][i] != 'Empty':
        result.append(snail_map[lap][i])
        snail_map[lap][i] = 'Empty'

# array = [[]]
# print('answer:', snail(array))
# print('soluti: []')
# array = [[1]]
# print('answer:', snail(array))
# print('soluti: [1]')
# array = [[1, 2],
#          [3, 4]]
# print('answer:', snail(array))
# print('soluti: [1, 2, 4, 3]')
# array = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]
# print('answer:', snail(array))
# print('soluti: [1, 2, 3, 6, 9, 8, 7, 4, 5]')
# array = [[1, 2, 3, 1],
#          [4, 5, 6, 4],
#          [7, 8, 9, 7],
#          [7, 8, 9, 7]]
# print('mine:', snail(array))
# print('notm: [1, 2, 3, 1, 4, 7, 7, 9, 8, 7, 7, 4, 5, 6, 9, 8]')
array = [[1, 2, 3, 4, 5, 6],
         [20, 21, 22, 23, 24, 7],
         [19, 32, 33, 34, 25, 8],
         [18, 31, 36, 35, 26, 9],
         [17, 30, 29, 28, 27, 10],
         [16, 15, 14, 13, 12, 11]]
print('mine:', snail(array))
print(
    'notm: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]')
