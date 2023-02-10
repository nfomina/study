class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

def is_good_password(string):
    if len(string) < 9:
        raise LengthError
    elif (any(c.islower() for c in string) and any(c.isupper() for c in string)) is False:
        raise LetterError
    elif any(c.isdigit() for c in string) is False:
        raise DigitError
    else:
        return True

try:
    print(is_good_password('Short7'))
except Exception as err:
    print(type(err))

print(is_good_password('еПQSНгиfУЙ70qE'))

try:
    print(is_good_password('41157081231232'))
except Exception as err:
    print(type(err))


try:
    print(is_good_password('abc12345678ansdfjkasdkjfbsdk'))
except Exception as err:
    print(type(err))