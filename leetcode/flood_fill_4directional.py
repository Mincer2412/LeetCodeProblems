from typing import List


def color_element(i, j, m, n, initial_color, new_color, image):
    if 0 <= i - 1 < m and image[i - 1][j] == initial_color:
        image[i - 1][j] = new_color
        color_element(i - 1, j, m, n, initial_color, new_color, image)

    if 0 <= j - 1 < n and image[i][j - 1] == initial_color:
        image[i][j - 1] = new_color
        color_element(i, j - 1, m, n, initial_color, new_color, image)

    if i + 1 < m and image[i + 1][j] == initial_color:
        image[i + 1][j] = new_color
        color_element(i + 1, j, m, n, initial_color, new_color, image)

    if j + 1 < n and image[i][j + 1] == initial_color:
        image[i][j + 1] = new_color
        color_element(i, j + 1, m, n, initial_color, new_color, image)


def flood_fill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    initial_color = image[sr][sc]
    image[sr][sc] = newColor

    if newColor == initial_color:
        return image

    color_element(sr, sc, len(image), len(image[sr]), initial_color, newColor, image)

    for row in image:
        print(row)

    return image


# flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
# flood_fill([[0, 0, 0], [0, 1, 0], [1, 0, 1]], 1, 1, 2)
# flood_fill([[0, 0, 0], [0, 0, 0]], 1, 1, 2)
flood_fill([[0, 0, 0], [0, 1, 1]], 1, 1, 1)
