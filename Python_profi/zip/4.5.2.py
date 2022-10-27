from zipfile import ZipFile

source_size = 0
compress_size = 0
with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    for item in info:
        if item.file_size:
            source_size += item.file_size
            if item.compress_size:
                compress_size += item.compress_size
            else:
                compress_size += item.file_size

print(f'Объем исходных файлов: {source_size} байт(а)')
print(f'Объем сжатых файлов: {compress_size} байт(а)')
