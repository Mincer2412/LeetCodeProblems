def is_equal_to_bad_version(n, bad_version):
    return n >= bad_version


def first_bad_version(n: int, bad_version: int) -> int:
    res_false = [-1, False]
    res_true = [-1, True]

    a = 1
    b = n

    while True:
        mid = (a + b) // 2

        bool_for_current = is_equal_to_bad_version(mid, bad_version)

        if bool_for_current:
            res_true = [mid, True]
        else:
            res_false = [mid, False]

        if [res_true[0] - 1, not res_true[1]] == res_false:
            return res_true[0]

        if bool_for_current:
            b = mid - 1
        else:
            a = mid + 1


print(first_bad_version(n=6, bad_version=6), 'should be equal to 6')
print(first_bad_version(n=6, bad_version=5), 'should be equal to 5')
print(first_bad_version(n=6, bad_version=4), 'should be equal to 4')
print(first_bad_version(n=6, bad_version=3), 'should be equal to 3')
print(first_bad_version(n=5, bad_version=2), 'should be equal to 2')
print(first_bad_version(n=6, bad_version=1), 'should be equal to 1')
print(first_bad_version(n=1, bad_version=1), 'should be equal to 1')
