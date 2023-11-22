def hash_function(obj):
    new_obj = str(obj)
    temp1 = 0
    temp2 = 0
    len_obj = len(new_obj)
    for i in range(len_obj//2):
        temp1 += ord(new_obj[i])*ord(new_obj[len_obj-i-1])
    if len_obj % 2 != 0:
        temp1 += ord(new_obj[len_obj//2])
    for j in range(len_obj):
        if j % 2 == 0:
            temp2 += ord(new_obj[j]) * (j + 1)
        else:
            temp2 -= ord(new_obj[j]) * (j + 1)
    return (temp1 * temp2) % 123456791


print(hash_function('python'))
# 111998846

print(hash_function(12345))
# 834432

print(hash_function(None))
