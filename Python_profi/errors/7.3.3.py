
try:
    with open(input()) as f:
        print(f.read())
except FileNotFoundError:
    print('Файл не найден')
