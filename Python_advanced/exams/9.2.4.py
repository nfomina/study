m = int(input())
n = int(input())

home_books = set()
for _ in range(m):
    home_books.add(input())

for _ in range(n):
    if input() in home_books:
        print('YES')
    else:
        print('NO')
