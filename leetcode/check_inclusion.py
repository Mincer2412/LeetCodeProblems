def put_in_dict(s: str) -> dict:
    d = dict()
    for letter in list(s):
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1

    return d


def check_inclusion(s1: str, s2: str) -> bool:
    len_s1 = len(s1)
    dict_s1 = put_in_dict(s1)
    for i in range(len(s2) - len_s1 + 1):
        print(s2[i:i + len_s1])
        dict_s2 = put_in_dict(s2[i:i + len_s1])
        if dict_s1 == dict_s2:
            return True

    return False


# print(check_inclusion('hello', 'ooolleoooleh'), 'should False')
# print(check_inclusion('ab', 'eidbao'), 'should True')
# print(check_inclusion('ab', 'eidboao'), 'should False')
# print(check_inclusion('abc', 'eidbcaok'), 'should True')
print(check_inclusion('abc', 'eidbcoaok'), 'should False')
# print(check_inclusion('adc', 'dcda'), 'should True')
