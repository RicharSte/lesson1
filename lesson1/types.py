def get_sum(one, two, delimiter = '&'):
    line = one + delimiter + two
    return line.upper()

print(get_sum('Learn','Python'))