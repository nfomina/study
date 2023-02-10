import sys


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


for line in sys.stdin:
    try:
        if is_good_password(line.strip()):
            print('Success!')
            break
    except Exception as e:
        print(e.__class__.__name__)
