def is_palindrome(string):
    if len(string) <= 1:
        return True
    elif string[0] != string[-1]:
        return False
    else:
        return is_palindrome(string[1:-1])


print(is_palindrome('stepik'))
print(is_palindrome('level'))
print(is_palindrome('122333221'))
