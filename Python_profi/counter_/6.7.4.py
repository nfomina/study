from collections import Counter

purchases = Counter(input().split(','))
max_len = len(max(purchases, key=lambda a: len(a)))
for item in sorted(purchases.items()):
    price = sum([ord(letter) for letter in item[0] if letter != ' '])
    print(f'{item[0]}{" "*(max_len - len(item[0]))}: {price} UC x {item[1]} = {price*item[1]} UC')

# <товар>: <цена за единицу товара> UC x <количество товаров в группе> = <общая стоимость группы> UC
# ord()

# банан: 5387 UC x 2 = 10774 UC
# груша: 5422 UC x 1 = 5422 UC
# киви : 4316 UC x 4 = 17264 UC
# лимон: 5418 UC x 3 = 16254 UC

# beauty
# from collections import Counter
#
# def get_price(product):
#     return sum(map(ord, filter(str.isalpha, product)))
#
# products = Counter(input().split(','))
# pattern = '{}: {} UC x {} = {} UC'
# spaces = max(map(len, products))
#
# for product, count in sorted(products.items()):
#     price = get_price(product)
#     total = price * count
#     product = product.ljust(spaces, ' ')
#     print(pattern.format(product, price, count, total))
