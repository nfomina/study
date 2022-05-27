# Реализуйте функцию beegeek(), которая принимает два целочисленных аргумента a и b, где a<b, и возвращает строку,
# составленную из чисел от a до b включительно или слов Bee, Geek и BeeGeek по следующему правилу:
#
# если число делится без остатка на 3, то вместо него в строку добавляется слово Bee;
# если число делится без остатка на 7, то вместо него в строку добавляется слово Geek;
# если число делится без остатка и на 3, и на 7, то вместо него в строку добавляется слово BeeGeek;
# в остальных случаях в строку добавляется само число.

def beegeek(a, b):
    res = []
    for i in range(a, b + 1):
        if i%3 == 0 and i%7 == 0:
            res.append('BeeGeek')
        elif i%3 == 0:
            res.append('Bee')
        elif i%7 == 0:
            res.append('Geek')
        else:
            res.append(str(i))
    return ' '.join(res)



print(beegeek(14, 21))

# Geek Bee 16 17 Bee 19 20 BeeGeek

print(beegeek(1, 2))

result = beegeek(10, 50)
print(result)

# 10 11 Bee 13 Geek Bee 16 17 Bee 19 20 BeeGeek 22 23 Bee 25 26 Bee Geek 29 Bee 31 32 Bee 34 Geek Bee 37 38 Bee 40 41 BeeGeek 43 44 Bee 46 47 Bee Geek 50