from datetime import datetime

older = ''
list_older = []
for _ in range(int(input())):
    name, family, date_birth = input().split()
    date_birth = datetime.strptime(date_birth, '%d.%m.%Y')
    if older:
        if date_birth < older:
            older = date_birth
            list_older = [(name, family)]
        elif date_birth == older:
            list_older.append(name)
    else:
        older = date_birth
        list_older.append((name,family))


count = len(list_older)
if count == 1:
    print(older.strftime('%d.%m.%Y'), list_older[0][0], list_older[0][1])
else:
    print(older.strftime('%d.%m.%Y'), count)

# 3
# Иван Петров 01.05.1995
# Петр Сергеев 29.04.1995
# Сергей Иванов 01.01.1996