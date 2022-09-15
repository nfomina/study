import sys

data = [int(i) for i in sys.stdin]
if data:
    print(f'''Рост самого низкого ученика: {min(data)}
Рост самого высокого ученика: {max(data)}
Средний рост: {sum(data)/len(data)}''')
else:
    print('нет учеников')