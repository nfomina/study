
templates = ['7-ddd-ddd-dd-dd', '8-ddd-dddd-dddd']


def is_phone_number(phone):
    if len(phone) == 15:
        if phone.startswith(('7-', '8-')):
            groups = phone.split('-')
            if (phone.startswith('7-') and len(groups[0]) == 1 and len(groups[1]) == 3 and len(groups[2]) == 3 and len(groups[3]) == 2
                and len(groups[4]) == 2) or (phone.startswith('8-') and len(groups[0]) == 1 and len(groups[1]) == 3 and len(groups[2]) == 4
                                             and len(groups[3]) == 4):

                chars = ''.join(groups)
                return all(c.isdigit() for c in chars)


def get_all_numbers(text):
    for c in range(len(text)):
        chunk = text[c:c + 15]
        if is_phone_number(chunk):
            yield chunk


for item in get_all_numbers(input()):
    print(item)

# INPUT DATA:

# TEST_1:
# Перезвони мне, пожалуйста: 7-919-667-21-19

# TEST_2:
# Артур: +7-919-667-21-19, Анри: 7-hey-anri-anri, Тимур: 8-917-4864-1911

# TEST_3:
# Тимур: 7-ddd-ddd-dd-dd, Сослан: 8-ddd-dddd-dddd, Артур: 7-123-123-11-22,,,, Дима: 8-123-123-11-22, Анри: 8-123-1231-1221...... Гвидо: 7-123-1231-1221, 7-123-13-181-22, 8-1237-131-1221

# OUTPUT DATA:

# TEST_1:
# 7-919-667-21-19

# TEST_2:
# 7-919-667-21-19
# 8-917-4864-1911

# TEST_3:
# 7-123-123-11-22
# 8-123-1231-1221