def is_integer(string):
    try:
        int(string)
        return True
    except:
        return False


print(is_integer('199'))
print(is_integer('-43'))
print(is_integer('5f'))
print(is_integer('5.0'))
print(is_integer('1.1'))
