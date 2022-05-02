# def first_non_repeating_letter(string):
#     for letter in string:
#         count = string.lower().count(letter.lower())
#         if count == 1:
#             return letter
#     return ''
#
# # def first_non_repeating_letter(string):
# #     dict = {}
# #
# #     for letter in range(len(string)):
# #         if string[letter] in dict:
# #             dict[string[letter]] = 2
# #         elif string[letter].upper() in dict:
# #             dict[string[letter].upper()] = 2
# #         elif string[letter].lower() in dict:
# #             dict[string[letter].lower()] = 2
# #         else:
# #             dict[string[letter]] = 1
# #
# #     dict = {k: v for k, v in dict.items() if dict[k] < 2}
# #
# #     return min(dict, key=dict.get) if dict else ''
#
#
# print(first_non_repeating_letter('a'))
# print(first_non_repeating_letter('aa'))
# print(first_non_repeating_letter('aaa'))
# print(first_non_repeating_letter('stress'))
# print(first_non_repeating_letter('abba'))
# print(first_non_repeating_letter(''))
# print(first_non_repeating_letter('sTreSS'))
# print(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'))


# Cant work with aaa aa and a tests
def first_non_repeating_letter(string):
    dict = {}

    for letter in range(len(string)):
        if string[letter] in dict:
            dict.pop(string[letter])
        elif string[letter].upper() in dict:
            dict.pop(string[letter].upper())
        elif string[letter].lower() in dict:
            dict.pop(string[letter].lower())
        else:
            dict[string[letter]] = 1

    return min(dict, key=dict.get) if dict else ''


print(first_non_repeating_letter('a'))
print(first_non_repeating_letter('aa'))
print(first_non_repeating_letter('aaa'))
