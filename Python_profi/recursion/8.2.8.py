def rec(number=1, count=16):
    if number < 4:
        print(' ' * int((16-count)/2), str(number)*count, sep='')
        number += 1
        count -= 4
        rec(number, count)
        print(' ' * int((16-count)/2), str(number)*count, sep='')
    if number == 2 and count == 12:
        print(str(number-1)*(count+4))


rec()


# 1111111111111111    # 16 раз
#   222222222222      # 12 раз
#     33333333        # 8 раз
#       4444          # 4 раза
#     33333333        # 8 раз
#   222222222222      # 12 раз
# 1111111111111111    # 16 раз

# universal
# def triangle(h):
#     def rec(n):
#         if n < h:
#             print((str(n) * (h - n + 1) * 4).rjust((h - n + 1) * 4 + (n - 1) * 2, ' ').ljust(h * 4, ' '))
#             rec(n + 1)
#         print((str(n) * (h - n + 1) * 4).rjust((h - n + 1) * 4 + (n - 1) * 2, ' ').ljust(h * 4, ' '))
#     rec(1)
#
# triangle(4)

