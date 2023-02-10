from collections import ChainMap, Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

ingredients = ChainMap(bread, meat, sauce, vegetables, toppings)

order = Counter(input().split(','))
max_item = max(order.keys(), key=lambda a: len(a))
max_len = len(max_item)
price = 0
for item, count in sorted(order.items()):
    print(f'{item}{" " * (max_len-len(item))} x {count}')
    price += ingredients.get(item) * count

max_len_order = max_len + 3 + len(str(order.get(max_item)))
string_price = f'ИТОГ: {price}р'
len_price = len(string_price)
print('-' * max([max_len_order, len_price]))
print(string_price)
