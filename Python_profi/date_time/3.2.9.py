from datetime import date
correct = 0
line = input()
while line != 'end':
    day, month, year = line.split('.')
    try:
        date(int(year), int(month), int(day))
        correct += 1
        print('Корректная')
    except:
        print('Некорректная')
    line = input()
print(correct)
