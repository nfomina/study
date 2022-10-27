from zipfile import ZipFile

res = []
with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    for item in info:
        if item.date_time >= (2021, 11, 30, 14, 22, 0):
            if item.filename.endswith('/') is False:
                res.append(item.filename.split('/')[-1])

for item in sorted(res):
    print(item)


# normal way
# with ZipFile('workbook.zip', mode='r') as file:
#     info = file.infolist()
#     compare = (2021, 11, 30, 14, 22, 0)
#
#     result = [i.filename.split('/')[-1] for i in info if i.date_time > compare and not i.is_dir()]
#
#     print(*sorted(result), sep='\n')
