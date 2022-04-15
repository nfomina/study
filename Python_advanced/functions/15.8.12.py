from functools import reduce

values = list(map(int, input().split()))
x = int(input())

def evaluate(coefficients, x):
    return reduce(lambda a, b: a + b, map(lambda a, b: a*(x**b), coefficients, [i for i in range(0, len(coefficients))][::-1]), 0)


print(evaluate(values, x))