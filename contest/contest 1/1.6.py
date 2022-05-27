
cards = [int(x) for x in input().split()]

if len(set(cards)) <= 1:
    print('Шулер')
else:
    counts = [cards.count(i) for i in cards]
    if max(counts) == 4:
        print('Каре')
    elif 2 in counts and 3 in counts:
        print('Фулл Хаус')
    elif sorted(cards) == [i for i in range(sorted(cards)[0], sorted(cards)[0]+5)]:
        print('Стрит')
    elif max(counts) == 3:
        print('Сет')
    elif counts.count(2) == 4:
        print('Две пары')
    elif max(counts) == 2:
        print('Пара')
    else:
        print('Старшая карта')


# Sample Input 1:
#
# 4 6 5 7 8
# Sample Output 1:
#
# Стрит
# Sample Input 2:
#
# 10 3 5 6 1
# Sample Output 2:
#
# Старшая карта
# Sample Input 3:
#
# 5 5 5 5 5
# Sample Output 3:
#
# Шулер
# Sample Input 4:
#
# 3 2 3 2 2
# Sample Output 4:
#
# Фулл Хаус
# Sample Input 5:
#
# 10 10 10 10 4
# Sample Output 5:
#
# Каре