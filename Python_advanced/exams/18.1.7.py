
mapping = {
    'а': 'a',
    'б': 'b',
    'в': 'v',
    'г': 'g',
    'д': 'd',
    'е': 'e',
    'ё': 'jo',
    'ж': 'zh',
    'з': 'z',
    'и': 'i',
    'й': 'j',
    'к': 'k',
    'л': 'l',
    'м': 'm',
    'н': 'n',
    'о': 'o',
    'п': 'p',
    'р': 'r',
    'с': 's',
    'т': 't',
    'у': 'u',
    'ф': 'f',
    'х': 'h',
    'ц': 'c',
    'ч': 'ch',
    'ш': 'sh',
    'щ': 'shh',
    'ъ': '*',
    'ы': 'y',
    'ь': '\'',
    'э': 'je',
    'ю': 'ju',
    'я': 'ya'}

with open('cyrillic.txt') as input_file, open('transliteration.txt', 'w') as output_file:
    text = input_file.read()
    for letter in text:
        if letter.islower():
            new_letter = mapping.get(letter, letter)
        elif letter.isupper():
            new_letter = mapping.get(letter.lower(), letter).capitalize()
        else:
            new_letter = letter
        output_file.write(new_letter)