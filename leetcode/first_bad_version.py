def is_equal_to_bad_version(n, bad_version):
    return n >= bad_version


def firstBadVersion(n: int, bad_version: int) -> int:
    a = 1
    b = n

    dic_res = {}

    while True:

        mid = (a + b) // 2

        if mid == 1 and is_equal_to_bad_version(mid, bad_version):
            return mid

        if a + 1 == b and is_equal_to_bad_version(b, bad_version):
            return b

        last_res = is_equal_to_bad_version(mid, bad_version)
        dic_res[mid] = last_res

        if last_res:
            if mid > 2 and mid - 1 in dic_res and dic_res[mid - 1] is False:
                return mid
            b = mid
        else:
            if mid >= 1 and mid + 1 in dic_res and dic_res[mid + 1] is True:
                return mid + 1
            a = mid


# print(firstBadVersion(n=5, bad_version=5), 'should be equal to 5')
# print(firstBadVersion(n=5, bad_version=4), 'should be equal to 4')
# print(firstBadVersion(n=5, bad_version=3), 'should be equal to 3')
# print(firstBadVersion(n=5, bad_version=2), 'should be equal to 2')
# print(firstBadVersion(n=5, bad_version=1), 'should be equal to 1')
# print(firstBadVersion(n=1, bad_version=1), 'should be equal to 1')

