
def is_valid(string):
    if len(string) in [4, 5, 6]:
        for item in string:
            if item.isdigit() is False:
                return False
        return True
    return False


print(is_valid('4367'))
print(is_valid('aaaa'))
print(is_valid('89abc1'))
print(is_valid('900876'))
print(is_valid('49 83'))
print(is_valid('467'))
print(is_valid('4323423424467'))
print(is_valid('3 7 0'))
print(is_valid('0000'))
print(is_valid(''))
print(is_valid('aaaa'))

# best
# def is_valid(pin):
#     return pin.isdigit() and len(pin) in (4, 5, 6)