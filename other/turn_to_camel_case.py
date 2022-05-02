def to_camel_case(text):
    if len(text) == 0:
        return text

    words = text.replace("_", " ").replace("-", " ").split("-").split("_")
    result = [words[0]]

    for i in range(1, len(words)):
        result.append(words[i].capitalize())

    return "".join(result)


print(to_camel_case('the_stealth_warrior'))
