s = input().split()

res = {}
for item in s:
    if item in res:
        res[item] = res.get(item, 0) + 1
        print(f'{item}_{res[item]}', end = ' ')
    else:
        res[item] = 0
        print(f'{item}', end = ' ')

#  beauty
# lst = input().split()
# res = {}
# for c in lst:
#     if c in res:
#         print(f'{c}_{res[c]}', end=' ')
#     else:
#         print(c, end=' ')
#     res[c] = res.get(c, 0) + 1