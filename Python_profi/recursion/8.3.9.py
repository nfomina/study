def tribonacci(n):
    cache = {1: 1, 2: 1, 3: 1}

    def tribonacci_rec(n):
        result = cache.get(n)
        if result is None:
            result = tribonacci_rec(n - 3) + tribonacci_rec(n - 2) + tribonacci_rec(n - 1)
            cache[n] = result
        return result
    return tribonacci_rec(n)


print(tribonacci(1))
print(tribonacci(7))
print(tribonacci(4))

# def fib(n):
#     ​cache = {1: 1, 2: 1}
#     def fib_rec(n):
#         result = cache.get(n)
#         if result is None:
#             result = fib_rec(n - 2) + fib_rec(n - 1)
#             cache[n] = result
#         return result
#     return fib_rec(n)
