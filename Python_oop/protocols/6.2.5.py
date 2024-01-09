class OrderedSet:
    def __init__(self, iterable=None):
        if iterable:
            self.items = dict.fromkeys(iterable, None)
        else:
            self.items = {}

    def add(self, item):
        if item not in self.items:
            self.items[item] = None

    def discard(self, item):
        if item in self.items:
            del self.items[item]

    def __getitem__(self, item):
        if item in self.items:
            return item

    def __iter__(self):
        yield from self.items

    def __len__(self):
        return len(self.items)

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return list(self.items) == list(other.items)
        elif isinstance(other, set):
            return self.items == dict.fromkeys(other, None)
        else:
            return NotImplemented


orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])

print(*orderedset)
print(len(orderedset))

orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])

print('python' in orderedset)
print('C++' in orderedset)

orderedset = OrderedSet()

orderedset.add('green')
orderedset.add('green')
orderedset.add('blue')
orderedset.add('red')
print(*orderedset)
orderedset.discard('blue')
orderedset.discard('white')
print(*orderedset)

# TEST_4:
print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['green', 'red', 'blue']))
print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['red', 'blue', 'green']))
print(OrderedSet(['green', 'red', 'blue']) == {'blue', 'red', 'green'})
print(OrderedSet(['green', 'red', 'blue']) == ['green', 'red', 'blue'])
print(OrderedSet(['green', 'red', 'blue']) == 100)

# TEST_5:
data = ['Ada Lovelace'] * 1000
orderedset = OrderedSet(data)

print(len(orderedset))

# TEST_6:
orderedset = OrderedSet([1, 2, 3, 4])
not_supported = [120, {1: 'one'}, True, 'pi = 3', 17.9]

for item in not_supported:
    print(item != orderedset)

# TEST_7:
orderedset = OrderedSet([1, 2, 3, 4])
print(orderedset.__eq__(1))
print(orderedset.__ne__(1.1))

