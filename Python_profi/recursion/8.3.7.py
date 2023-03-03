def recursive_sum(a, b):
    if a <= 0:
        return b
    else:
        return recursive_sum(a-1, b+1)


print(recursive_sum(10, 22))
print(recursive_sum(99, 0))
print(recursive_sum(0, 0))
