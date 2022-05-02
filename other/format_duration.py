def format_duration(seconds):
    result = {}

    if seconds > 0:
        result['seconds'] = seconds % 60
        seconds = seconds // 60

    if seconds > 0:
        result['minutes'] = seconds % 60
        seconds = seconds // 60

    if seconds > 0:
        result['hours'] = seconds % 24
        seconds = seconds // 24

    if seconds > 0:
        result['days'] = seconds % 365
        seconds = seconds // 365

    if seconds > 0:
        result['years'] = seconds

    return reformat_date(result) if result else 'now'


def reformat_date(dictionary):
    res = ''

    if 'years' in dictionary:
        res += str(dictionary['years']) + ' year'
        if dictionary['years'] > 1:
            res += 's'

    if 'days' in dictionary:
        res += ' ' + str(dictionary['days']) + ' day'
        if dictionary['days'] > 1:
            res += 's'

    if 'hours' in dictionary:
        res += ' ' + str(dictionary['hours']) + ' hour'
        if dictionary['hours'] > 1:
            res += 's'

    if 'minutes' in dictionary and dictionary['minutes'] > 0:
        res += ' ' + str(dictionary['minutes']) + ' minute'
        if dictionary['minutes'] > 1:
            res += 's'

    if 'seconds' in dictionary and dictionary['seconds'] > 0:
        if dictionary['seconds'] == 1:
            res += ' ' + str(dictionary['seconds']) + ' second'
        else:
            res += str(dictionary['seconds']) + ' seconds'

    return res


# print(format_duration(0))
# print(format_duration(50))
# print(format_duration(60))
# print(format_duration(61))
# print(format_duration(122))
# print(format_duration(7200))
# print(format_duration(3662))
# print(format_duration(86400))
# print(format_duration(90000))
# print(format_duration(100 * 24 * 60 * 60 + 3601))
print(format_duration(365 * 24 * 60 * 60 + 3661))
