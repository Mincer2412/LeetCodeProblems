def who_is_next(names, n):
    l = round((n + 5 + 0.1) / 2)  # round to upper gen
    gen = 40
    l = gen  # remove
    l_start = l - 4
    step = int(l / 5)

    line = [names[0]] * step + [names[1]] * step + [names[2]] * step + [names[3]] * step + [names[4]] * step

    print(step)
    return line[n - l_start]


print(who_is_next(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 14))
