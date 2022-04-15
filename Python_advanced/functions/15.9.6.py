password = input()

print((lambda x: 'YES' if len(password) >= 7 and any([i for i in password if i.isdigit()]) and \
                          any([i for i in password if i.isupper()]) and \
                          any([i for i in password if i.islower()]) else 'NO')(password))


#  so beauty
# s = input()
# print('YES' if all((any(i.isupper() for i in s),
#                     any(i.islower() for i in s),
#                     any(i.isdigit() for i in s),
#                     len(s) >= 7)) else 'NO')