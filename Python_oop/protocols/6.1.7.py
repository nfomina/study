class LoopTracker:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.collection = list(iterable)
        self.length = len(list(iterable))
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        return next(self.iterable)

    @property
    def accesses(self):
        if self.counter <= self.length:
            return self.counter
        return self.length

    @property
    def empty_accesses(self):
        if self.counter > self.length:
            return self.counter - self.length
        return 0

    @property
    def first(self):
        if self.collection:
            return self.collection[0]
        raise AttributeError('Исходный итерируемый объект пуст')

    @property
    def last(self):
        if self.counter == 0:
            raise AttributeError('Последнего элемента нет')
        return self.collection[self.counter - 1]

    def is_empty(self):
        if self.counter >= self.length:
            return True
        return False


loop_tracker = LoopTracker([1, 2, 3])

print(next(loop_tracker))
print(list(loop_tracker))

loop_tracker = LoopTracker([1, 2, 3])

print(loop_tracker.accesses)
next(loop_tracker)
next(loop_tracker)
print(loop_tracker.accesses)

loop_tracker = LoopTracker([1, 2, 3])
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)

loop_tracker = LoopTracker([1, 2, 3])

print(next(loop_tracker))
print(loop_tracker.last)

print(next(loop_tracker))
print(loop_tracker.last)

print(next(loop_tracker))
print(loop_tracker.last)