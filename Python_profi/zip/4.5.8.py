from zipfile import ZipFile


def extract_this(zip_name, *args):
    with ZipFile(zip_name) as zip_file:
        if args:
            for item in args:
                zip_file.extract(item)
        else:
            zip_file.extractall()


extract_this('workbook.zip')