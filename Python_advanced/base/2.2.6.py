n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

number = int(input())
answer = ''

for i in range(n):
    for j in range(n):
        if i != j and numbers[i] * numbers[j] == number:
            answer = 'ДА'
            break

if answer:
    print(answer)
else:
    print('НЕТ')
