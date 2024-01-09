class SkipIterator:
    def __init__(self, iterable, n):
        self.iterable = iter(iterable)
        self.n = n+1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = next(self.iterable)
        while self.count < self.n and self.count != 0:
            self.count += 1
            value = next(self.iterable)
        self.count = 1
        return value


# TEST_1:
skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)   # пропускаем по одному элементу

print(*skipiterator)

# TEST_2:
skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)   # пропускаем по два элемента

print(*skipiterator)

# TEST_3:
skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)   # не пропускаем элементы

print(*skipiterator)

# TEST_4:
skipiterator = SkipIterator('abcd', 0)

print(*skipiterator)

# TEST_5:
skipiterator = SkipIterator(['abcd'], 1)

print(*skipiterator)

# TEST_6:
skipiterator = SkipIterator('abcd', 3)

print(*skipiterator)

# TEST_7:
skipiterator = SkipIterator(iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)

print(*skipiterator)

# TEST_8:
skipiterator = SkipIterator(iter(['aa', 'bb', 'cc', 'dd', 'ee', 'ff']), 2)

print(*skipiterator)

# TEST_9:
data = ['к', 'б', 'ш', 'к', 'к', 'о', 'т', 'г', 'о', 'д', 'р', 'в', 'с', 'с', 'и', 'о', 'в', 'п', 'у', 'с', 'л', 'т',
        'г', 'т', 'з', 'ь', 'о', 'п', 'н', 'в', 'и', 'н', 'с', 'п', 'р', 'ш', 'е', 'к', 'н', 'с', 'у', 'в', 'п', 'т',
        'х', 'т', 'с', 'с', 'л', 'с']
skipiterator = SkipIterator(iter(data), 4)

print(*skipiterator)

# TEST_10:
skipiterator = SkipIterator(range(1000), 7)

for _ in range(25):
    next(skipiterator)

print(next(skipiterator))
print(next(skipiterator))
print(next(skipiterator))

