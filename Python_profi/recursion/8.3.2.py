def f(n, sum_=0):
    return sum_ if not n else f(str(n)[:-1], sum_=sum_ + int(str(n)[-1]))


print(f(int(input())))


# beauty
# def recursive_sum(number):
#     if not number:
#         return 0
#     return number % 10 + recursive_sum(number // 10)
#
# print(recursive_sum(int(input())))
