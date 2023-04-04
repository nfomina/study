from functools import lru_cache


@lru_cache(typed=False)
def ways(n):
    if n == 1:
        return 1
    elif n < 0:
        return 0
    else:
        return ways(n-1) + ways(n-3) + ways(n-4)


# TEST_1:
print(ways(5))

# TEST_2:
print(ways(1))

# TEST_3:
print(ways(2))

# TEST_4:
print(ways(50))

# TEST_5:
print(ways(100))

# TEST_6:
print(ways(4))

# TEST_7:
print(ways(3))

# TEST_8:
print(ways(6))

# TEST_9:
print(ways(7))
