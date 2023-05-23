def reverse(sequence):
    sequence = list(sequence)
    while sequence:
        yield sequence.pop()


print(*reverse([1, 2, 3, 4, 5]))

generator = reverse('beegeek')

print(type(generator))
print(*generator)

# smart
# def reverse(sequence):
#     yield from reversed(sequence)
