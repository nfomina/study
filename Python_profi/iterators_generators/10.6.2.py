def is_prime(number):
    if number == 1:
        return False
    else:
        generator = (i for i in range(2, number) if number % i == 0)
        try:
            next(generator)
            return False
        except StopIteration:
            return True


print(is_prime(7))
print(is_prime(8))
print(is_prime(1))

# smart
# def is_prime(number: int) -> bool:
#     return number != 1 and all(number % i != 0 for i in range(2, round(number**0.5)+1))
