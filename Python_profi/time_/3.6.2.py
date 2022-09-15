import time

def get_the_fastest_func(funcs, arg):
    time_func = {}
    for func in funcs:
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        time_func[func] = end-start
    return min(time_func, key=time_func.get)


def for_and_append(iterable):  # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension(iterable):  # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function(iterable):  # с использованием встроенной функции list()
    return list(iterable)

print(get_the_fastest_func([for_and_append, list_comprehension, list_function], range(100_000)))