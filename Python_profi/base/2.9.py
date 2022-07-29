from itertools import groupby

files = []

def key_func(k):
    return k['extension']

def calculate_size(size, name):
    mapping = {
        'B': 1,
        'KB': 1024,
        'MB': 1024*1024,
        'GB': 1024*1024*1024
    }
    return int(size)*mapping.get(name)

def nornmal_size(bytes):
    gb = round(bytes / 1073741824)
    if gb >= 1:
        return f'{gb} GB'
    else:
        mb = round(bytes / 1048576)
        if mb >=1:
            return f'{mb} MB'
        else:
            kb = round(bytes / 1024)
            if kb >= 1:
                return f'{kb} KB'
            else:
                return f'{bytes} B'

with open('files.txt', encoding = 'utf-8') as f:
    for line in f.readlines():
        full_name, size, letter = line.split()
        files.append({'name': full_name,
                      'extension': full_name.split('.')[-1],
                      'size_in_B': calculate_size(size, letter)})

files = sorted(files, key=key_func)
for key, value in groupby(files, key_func):
    files = list(value)
    total_size = sum(item['size_in_B'] for item in files)
    sorted_list = sorted(files, key=lambda x: x['name'])
    for item in sorted_list:
        print(item['name'])
    print('----------')
    print(f'Summary: {nornmal_size(total_size)}')
    print()


# without bicycles
# dict_names = {}
# dict_size = {}
# dict_dimension = {'B': 1, 'KB': 1024, 'MB': 1048576, 'GB': 1073741824}
# with open("files.txt", 'r', encoding='utf-8') as file:
#     for line in file.readlines():
#         # разделяем на нужные нам слова
#         name, size, dimension = line.split()
#         name, extension = name.split('.')
#         # заполняем словарь с именами по расширениям
#         dict_names[extension] = (dict_names.get(extension, []) +
#                                  [name + '.' + extension])
#         # заполняем словарь с размерами по расширениям
#         dict_size[extension] = (dict_size.get(extension, 0) +
#                                  dict_dimension[dimension] * int(size))
#
#     for extension in sorted(dict_names):
#         print(*sorted(dict_names[extension]), sep='\n')
#         print('----------')
#         for key in dict_dimension:
#             result = dict_size[extension] / dict_dimension[key]
#             if result <= 1024:
#                 break
#         print('Summary:', round(result), key)
#         print()