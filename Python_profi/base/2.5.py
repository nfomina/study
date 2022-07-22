n = int(input())

numbers = [i for i in range(1, n+1)]

res = {}
for number in numbers:
    sum = 0
    for item in str(number):
        sum += int(item)
    if sum in res:
        res[sum].append(number)
    else:
        res[sum] = [number]

print(len(max(res.values(), key=lambda k: len(k))))

# short
# data = {}
#
# for i in range(1, int(input()) + 1):
#     sum_of_digits = sum(map(lambda d: int(d), str(i)))
#     data[sum_of_digits] = data.get(sum_of_digits, 0) + 1
#
# print(max(data.values()))