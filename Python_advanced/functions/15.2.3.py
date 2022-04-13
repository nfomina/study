from statistics import mean as mean_

def mean(*args):
    numbers = []
    for arg in args:
        if type(arg)==int or type(arg)==float:
            numbers.append(arg)
    if numbers:
        return float(mean_(numbers))
    else:
        return 0.0

print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# 0.0
# 7.0
# 2.0
# 0.0
# 3.5
# 5.5