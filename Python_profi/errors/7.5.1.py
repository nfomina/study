# его длина равна 9 или более символам
# в нем присутствуют большие и маленькие буквы любого алфавита
# в нем имеется хотя бы одна цифра



def is_good_password(string):
    if len(string) >= 9 and any(i.isdigit() for i in string) and any(i.istitle() for i in string) and \
            any(i.islower() for i in string):
        return True
    return False


print(is_good_password('41157082'))
print(is_good_password('мойпарольсамыйлучший'))
print(is_good_password('МойПарольСамыйЛучший111'))


# such beauty
# def is_good_password(s: str):
#     if all(
#         (len(s) >= 9,
#          any(c.islower() for c in s),
#          any(c.isupper() for c in s),
#          any(c.isdigit() for c in s))
#             ):
#         return True
#     else:
#         return False
