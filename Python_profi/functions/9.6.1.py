def get_digits(number) -> list:
    return [int(x) for x in str(number) if x.isdigit()]


print(get_digits(16733))

print(get_digits(13.909934))

annotations = get_digits.__annotations__

print(annotations['return'])

# python 3.10
# def get_digits(number: int|float) -> list[int]:
#     return [int(x) for x in str(number) if x.isdigit()]
