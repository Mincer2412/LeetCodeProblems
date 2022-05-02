def sort_array(arr):
    odds = []
    print(arr)

    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            odds.append(arr[i])
            arr[i] = None

    odds.sort()

    for i in range(len(arr)):
        if arr[i] is None:
            arr[i] = odds.pop(0)

    return arr


print(sort_array([7, 1, 2, 8, 5, 4]))
