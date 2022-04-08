n = int(input())

one = 0
two = 0
three = 0
four = 0

for i in range(n):
    x, y = input().split()
    if int(x) > 0:
        if int(y) > 0:
            one += 1
        elif int(y) < 0:
            four += 1
    elif int(x) < 0:
        if int(y) > 0:
            two += 1
        elif int(y) < 0:
            three += 1

print(f'''Первая четверть: {one}
Вторая четверть: {two}
Третья четверть: {three}
Четвертая четверть: {four}''')