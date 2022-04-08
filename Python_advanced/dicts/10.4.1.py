n = int(input())

python_dict = {}
for _ in range(n):
    word, definition = input().split(': ')
    python_dict[word.lower()] = definition

m = int(input())
for _ in range(m):
    word = input().lower()
    print(python_dict.get(word, 'Не найдено'))