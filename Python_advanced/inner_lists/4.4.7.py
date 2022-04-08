n = int(input())
matrix = []

for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

sum_top = 0
sum_left = 0
sum_right = 0
sum_bottom = 0
for i in range(n):
    for j in range(n):
        if i > j and i < n-1-j:
            sum_left += matrix[i][j]
        elif i < j and i > n-1-j:
            sum_right += matrix[i][j]
        elif i < j and i < n-1-j:
            sum_top += matrix[i][j]
        elif i > j and i > n-1-j:
            sum_bottom += matrix[i][j]

print(f'''Верхняя четверть: {sum_top}
Правая четверть: {sum_right}
Нижняя четверть: {sum_bottom}
Левая четверть: {sum_left}''')