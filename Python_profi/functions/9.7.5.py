def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            value = func(*args, **kwargs)
        except Exception as ex:
            value = None
        if value:
            return (value, 'Функция выполнилась без ошибок')
        else:
            return (None, 'При вызове функции произошла ошибка')
    return wrapper


@exception_decorator
def f(x):
    return x ** 2 + 2 * x + 1


print(f(7))
sum = exception_decorator(sum)

print(sum(['199', '1', 187]))
