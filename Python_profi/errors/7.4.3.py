import json

try:
    with open(input(), encoding='utf-8') as file:
        print(json.load(file))
except FileNotFoundError:
    print('Файл не найден')
except Exception:
    print('Ошибка при десериализации')
