n = int(input())

info = {}
for _ in range(n):
    phone, name = input().split()
    if name.lower() in info:
        info[name.lower()].append(phone)
    else:
        info[name.lower()] = [phone]

m = int(input())
for _ in range(m):
    res = info.get(input().lower())
    if res:
        print(*res)
    else:
        print('абонент не найден')

# short
# dct = {}
# for _ in range(int(input())):
#     phone, name = input().lower().split()
#     dct.setdefault(name, []).append(phone)
# for _ in range(int(input())):
#     print(*dct.get(input().lower(), ['абонент не найден']))