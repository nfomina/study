class ReversedSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, key):
        key = self.__len__() - key - 1
        return self.sequence[key]

    def __contains__(self, item):
        return item in self.cart

    def __iter__(self):
        yield from reversed(list(self.sequence))

    def __setitem__(self, key, value):
        key = self.__len__() - key - 1
        self.sequence[key] = value

    def __delitem__(self, key):
        key = self.__len__() - key - 1
        del self.sequence[key]


reversed_list = ReversedSequence([1, 2, 3, 4, 5])

print(reversed_list[0])
print(reversed_list[1])
print(reversed_list[2])

numbers = [1, 2, 3, 4, 5]
reversed_numbers = ReversedSequence(numbers)

print(reversed_numbers[0])
numbers.append(6)
print(reversed_numbers[0])

numbers = [1, 2, 3, 4, 5]
reversed_numbers = ReversedSequence(numbers)
print(len(reversed_numbers))

numbers.append(6)
numbers.append(7)
print(len(reversed_numbers))

# TEST_4:
reversed_numbers = ReversedSequence((1, 2, 3, 4, 5))

for num in reversed_numbers:
    print(num)

# TEST_5:
reversed_chars = ReversedSequence('abcde')

for char in reversed_chars:
    print(char)

# TEST_6:
reversed_chars = ReversedSequence('abcdefghijklmnopqrstuvwxyz')

print(reversed_chars[0], reversed_chars[7], reversed_chars[11], reversed_chars[25])

# TEST_7:
reversed_list = ReversedSequence(['Gvido', 'Elon', 'Gates', 'Jobs', 'Zuckerberg'])

print(*reversed(reversed_list))
