class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.start = -1
        self.end = len(iterable)


    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end-1:
            self.start += 1
        else:
            self.start = 0
        return self.iterable[self.start]


cycle = Cycle('be')

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))

cycle = Cycle([1])

print(next(cycle) + next(cycle) + next(cycle))

cycle = Cycle(range(100_000_000))

print(next(cycle))
print(next(cycle))

# smart
# class Cycle:
#
#     def __init__(self, obj):
#         self.obj = obj
#         self.it = iter(self.obj)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         try:
#             return next(self.it)
#         except StopIteration:
#             self.it = iter(self.obj)
#             return next(self.it)
