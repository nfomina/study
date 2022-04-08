n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)
answer = 'YES'

numbers = set()
for item in matrix:
    numbers.update(item)

for number in numbers:
    if number < 1 or number > n*n:
        answer = 'NO'

if answer != 'NO':
    if len(numbers) != n*n:
        answer = 'NO'
    else:
        sum_ = 0
        for i in range(n):
            sum_ += matrix[i][i]

        for item in matrix:
            if sum(item) != sum_:
                answer = 'NO'
                break

        sum_diag = 0
        for i in range(n):
            sum_diag += matrix[i][n-i-1]
        if sum_diag != sum_:
            answer = 'NO'

        matrix.reverse()
        for item in matrix:
            if sum(item) != sum_:
                answer = 'NO'
                break

print(answer)

#
# amazing
#
# n = int(input())
# a = [[*map(int, input().split())] for _ in range(n)]
# print(('NO', 'YES')[set(sum(a, [])) == set((*range(1, n ** 2 + 1),))   # ряд натур. чисел до n ** 2
#                     and
#                     len(set(map(sum, (*a,                              # суммы строк
#                                   *zip(*a),                            # суммы столбцов (транспон-ый кв-т)
#                                   [a[i][i] for i in range(n)],         # сумма гл. диагоналей
#                                   [a[i][~i] for i in range(n)]))       # сумма втор. диагонали
#                        )) == 1])