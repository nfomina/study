fib = lambda a: 1 if a in (1, 2) else fib(a-1) + fib(a-2)

print(fib(1))
print(fib(2))
print(fib(5))

# Memoization
# d = {1: 1, 2: 1}
# fib = lambda x: d[x] if x in d else d.setdefault(x, fib(x - 1) + fib(x - 2))
