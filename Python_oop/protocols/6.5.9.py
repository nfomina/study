import copy


class Atomic:
    def __init__(self, data, deep=False):
        self._data = data
        self._deep = deep

    def __enter__(self):
        if not self._deep:
            self._new_data = copy.copy(self._data)
        else:
            self._new_data = copy.deepcopy(self._data)
        if isinstance(self._data, set):
            self._new_data = set(self._new_data)
        return self._new_data

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            if isinstance(self._data, list):
                self._data[:] = self._new_data
            else:
                self._data.clear()
                self._data.update(self._new_data)
        return True


numbers = [1, 2, 3, 4, 5]

with Atomic(numbers) as atomic:
    atomic.append(6)
    atomic[2] = 0
    del atomic[1]

print(numbers)

numbers = [1, 2, 3, 4, 5]

with Atomic(numbers) as atomic:
    atomic.append(6)
    atomic[2] = 0
    del atomic[100]           # обращение по несуществующему индексу

print(numbers)

matrix = [[1, 2], [3, 4]]

with Atomic(matrix) as atomic:
    atomic[1].append(0)       # изменение вложенной структуры
    atomic.append([5, 6])
    del atomic[100]           # обращение по несуществующему индексу

print(matrix)

matrix = [[1, 2], [3, 4]]

with Atomic(matrix, True) as atomic:
    atomic[1].append(0)       # изменение вложенной структуры
    atomic.append([5, 6])
    del atomic[100]           # обращение по несуществующему индексу

print(matrix)