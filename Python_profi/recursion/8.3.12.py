def counter(n):
    if n > 0:
        print(n)
        counter(n-5)
    print(n)


counter(int(input()))

# counter(16)
# counter(10)
# counter(1)

# 16
# 11
# 6
# 1
# -4
# 1
# 6
# 11
# 16
