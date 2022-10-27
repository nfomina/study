from zipfile import ZipFile


def convert_bytes(size):
    """Конвертер байт в большие единицы"""
    if size < 1000:
        return f'{size} B'
    elif 1000 <= size < 1000000:
        return f'{round(size / 1024)} KB'
    elif 1000000 <= size < 1000000000:
        return f'{round(size / 1048576)} MB'
    else:
        return f'{round(size / 1073741824)} GB'

with ZipFile('desktop.zip') as zip_file:
    info = zip_file.infolist()
    for item in info:
        if item.is_dir():
            print(f'{"  "*(len(item.filename.split("/"))-2)}{item.filename.split("/")[-2]}')
        else:
            print(f'{"  "*(len(item.filename.split("/"))-1)}{item.filename.split("/")[-1]} {convert_bytes(item.file_size)}')

# test
#   Картинки
#     1.jpg 88 KB
#     avatar.png 19 KB
#     certificate.png 43 KB
#     py.png 33 KB
#     World_Time_Zones_Map.png 2 MB
#     Снимок экрана.png 11 KB
#   Неравенства.djvu 5 MB
#   Программы
#     image_util.py 5 KB
#     sort.py 61 B
#   Разные файлы
#     astros.json 505 B

# so short
# from zipfile import ZipFile
#
# def hr_size(n, k = 0):
#     return f"{round(n)} {['B', 'KB', 'MB', 'GB', 'TB'][k]}" if n < 1024 else hr_size(n / 1024, k + 1)
#
# with ZipFile('workbook.zip') as z:
#     for i in z.infolist():
#         p = i.filename.strip('/').split('/')
#         print('  ' * (len(p) - 1) + p[-1] + ('' if i.is_dir() else ' ' + hr_size(i.file_size)))
