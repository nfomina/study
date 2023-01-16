from collections import Counter


books = Counter(input().split())
money = 0
for _ in range(int(input())):
    book, price = input().split()
    if books.get(book):
        books = books - Counter({book: 1})
        money += int(price)
print(money)

# 1 1 11 9 5 5 7 9 9
# 7
# 1 300
# 1 250
# 11 400
# 1 300
# 7 200
# 9 400
# 7 250

# smart
#
# books = Counter(map(int, input().split()))
# total = 0
#
# for _ in range(int(input())):
#     book, price = map(int, input().split())
#     total += bool(books[book]) * price
#     books -= Counter({book: 1})
#
# print(total)
