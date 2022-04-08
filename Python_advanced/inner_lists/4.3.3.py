def pascal(number_line):
    if number_line == 0:
        return [1]
    elif number_line == 1:
        return [1, 1]
    list = []
    for n in range(number_line+1):
        list.append([])
        list[n].append(1)
        for m in range(1, n):
            list[n].append(list[n - 1][m - 1] + list[n - 1][m])
        if (number_line != 0):
            list[n].append(1)
    return (list[number_line])

print(pascal(int(input())))