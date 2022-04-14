import math

mapping_command =  {
    'квадрат': lambda x: x**2,
    'куб': lambda x: x**3,
    'корень': lambda x: x**0.5,
    'модуль': lambda x: abs(x),
    'синус': lambda x: math.sin(x)
}

n = int(input())
print(mapping_command.get(input())(n))