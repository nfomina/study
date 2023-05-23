def primes(left, right):
    while left <= right:
        if left > 1:
            if all(left % x != 0 for x in range(2, int(left**.5)+1)):
                yield left
        left += 1


generator = primes(1, 15)

print(*generator)

generator = primes(6, 36)

print(next(generator))
print(next(generator))
