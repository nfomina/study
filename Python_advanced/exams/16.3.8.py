import operator

mapping = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

def arithmetic_operation(operator):
    return mapping.get(operator)




add = arithmetic_operation('+')
print(add)
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))