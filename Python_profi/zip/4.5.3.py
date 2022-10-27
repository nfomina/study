from zipfile import ZipFile

best = 100
with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    for item in info:
        if item.file_size and item.compress_size:
            res = item.compress_size/item.file_size * 100
            if res <= best:
                name = item.filename
                best = res
print(name.split('/')[-1])
