from zipfile import ZipFile
from datetime import datetime

res = []
with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    for item in info:
        if item.is_dir() is False:
            res.append([item.filename.split('/')[-1], item.date_time, item.file_size, item.compress_size])

for item in sorted(res):
    print(item[0])
    print(f'  Дата модификации файла: {datetime(*item[1])}')
    print(f'  Объем исходного файла: {item[2]} байт(а)')
    print(f'  Объем сжатого файла: {item[3]} байт(а)')
    print()
