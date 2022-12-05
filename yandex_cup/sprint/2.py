# t = int(input())
#
# for i in range(t):
#     count = 0
#     n, b = map(int, input().split())
#     for item in range(1, n+1):
#         vasua_res = ''
#         for number in str(item):
#             vasua_res += str(int(number)//b)
#         if int(vasua_res) == item/b:
#             count += 1
#     print(count)


import math

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

# t = int(input())
#
# for i in range(t):
#     n, b = map(int, input().split())
result = list(filter(lambda x: (x % 7 == 0), [i for i in range(1, 1000000000000000000)]))
print(result)