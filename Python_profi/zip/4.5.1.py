from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    print(sum([not item.is_dir() for item in zip_file.infolist()]))
