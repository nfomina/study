import re


def normalize_jpeg(filename):
    return re.sub(r'\.\w{3,4}$', '.jpg', filename)


print(normalize_jpeg('stepik.jPeG'))
print(normalize_jpeg('mountains.JPG'))
print(normalize_jpeg('windows11.jpg'))
print(normalize_jpeg('jepg_file.jPG'))
print(normalize_jpeg('file_jepg.jPeG'))
print(normalize_jpeg('file.jepg.JPEG'))
print(normalize_jpeg('filename.jpg.jpg'))
print(normalize_jpeg('stepik.jpeg.jpeg'))
print(normalize_jpeg('stepik.jpg.jpeg'))
print(normalize_jpeg('stepik.jpeg.jpg'))
print(normalize_jpeg('beegeek.JPg'))
print(normalize_jpeg('нарусском.JPg'))
print(normalize_jpeg('на русском языке.JPG'))
print(normalize_jpeg('jpg.jPg.Jpg.JPG'))
print(normalize_jpeg('Это тест.JpEg'))
