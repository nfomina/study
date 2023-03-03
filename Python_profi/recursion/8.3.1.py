def number_count(number, len_=0):
    if not number:
        return len_
    else:
        len_ += 1
        return number_count(number[:-1], len_)


print(number_count(input()))


# beauty
# def f(n):
#     return 1 if 0 <= n <= 9 else 1 + f(n // 10)
# print(f(int(input())))
