def limited_hash(left, right, hash_function=hash):
    def hash_f(arg):
        res_f = hash_function(arg)
        while res_f < left or res_f > right:
            if res_f > right:
                res_f = left + (res_f - right) % (right - left + 1) - 1
                if res_f < left:
                    res_f = right
            elif res_f < left:
                res_f = right - (left - res_f - 1) % (right - left + 1)
            else:
                pass
            return res_f
        return hash_function(arg)
    res = hash_f
    return res



hash_function = limited_hash(10, 15)

print(hash_function(10))
print(hash_function(11))
print(hash_function(15))
# Sample Output 1:
#
# 10
# 11
# 15
print('-' * 20)
hash_function = limited_hash(10, 15)

print(hash_function(16))
print(hash_function(17))
print(hash_function(21))
print(hash_function(22))
print(hash_function(23))
# Sample Output 2:
#
# 10
# 11
# 15
# 10
# 11
print('-' * 20)
hash_function = limited_hash(10, 15)

print(hash_function(9))
print(hash_function(8))
print(hash_function(4))
print(hash_function(3))
print(hash_function(2))

# 15
# 14
# 10
# 15
# 14

# TEST_4:
hash_function = limited_hash(2, 3, hash_function=lambda obj: len(str(obj)))

print(hash_function('a'))
print(hash_function('ab'))
print(hash_function('abc'))
print(hash_function('abcd'))
print(hash_function('abcde'))
print(hash_function('abcdef'))
print(hash_function('abcdefg'))

# TEST_5:
def hash_function(obj):
    return sum(index * ord(character) for index, character in enumerate(str(obj), start=1))


hash_function = limited_hash(10, 15, hash_function)

array = [1366, -5502567186.7395, 'zZQyrjYzdgcabTZPATPl', False, {'монета': -671699723096.267, 'лететь': 5151},
         (False, True, 897, -844416.51017117, 1101),
         [True, 171664.794743347, True, False, 'UypAaBSjBWYWBYbmRTdN', 4044844490314.56]]

for item in array:
    print(hash_function(item))

# beauty
# def limited_hash(left, right, hash_function=hash):
#     def inner_hash_function(obj):
#         hash_value = hash_function(obj)
#         if hash_value < left:
#             hash_value = right - (left - hash_value - 1) % (right - left + 1)
#         elif hash_value > right:
#             hash_value = left + (hash_value - right - 1) % (right - left + 1)
#         return hash_value
#     return inner_hash_function
