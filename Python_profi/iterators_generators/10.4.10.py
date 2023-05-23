class Alphabet:
    def __init__(self, language):
        self.language = language
        if self.language == 'ru':
            self.alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        else:
            self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.it = iter(self.alphabet)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.it)
        except StopIteration:
            self.it = iter(self.alphabet)
            return next(self.it)



ru_alpha = Alphabet('ru')

print(next(ru_alpha))
print(next(ru_alpha))
print(next(ru_alpha))

en_alpha = Alphabet('en')

letters = [next(en_alpha) for _ in range(28)]

print(*letters)
