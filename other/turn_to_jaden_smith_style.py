def to_jaden_case(string):
    return " ".join(map(lambda s: s.capitalize(), string.split()))


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
