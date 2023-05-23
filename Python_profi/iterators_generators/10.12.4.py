from collections import namedtuple
from itertools import combinations

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]

weight = int(input())
all_combinations = []
for r in range(1, len(items)+1):
    for item in combinations(items, r):
        if sum([el.mass for el in item]) <= weight:
            all_combinations.append([item])

max = 0
best_bag = []
for bag in all_combinations:
    for items in bag:
        if sum([el.price for el in items]) > max:
            max = sum([el.price for el in items])
            best_bag = bag

if best_bag:
    for item in sorted(best_bag[0], key=lambda a: a.name):
        print(item.name)
else:
    print('Рюкзак собрать не удастся')


# TEST_15:
# 9000
#
# # TEST_16:
# 400
#
# # TEST_17:
# 600
#
# # TEST_18:
# 700
#
# # TEST_19:
# 1200
#
# # TEST_20:
# 1300
