d = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}

sentence = input()
for item in sentence:
    for number, letters in d.items():
        if item.upper() in letters:
            count = letters.index(item.upper())
            print(number*(count+1), end = '')
