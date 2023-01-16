class Lexicon:
    def __init__(self):
        self.array = list()

    # Return True if Lexicon contains word, otherwise return False
    def find(self, word):
        if word in self.array:
            return True
        return False

    # Insert word into Lexicon (return nothing)
    def insert(self, word):
        self.array.append(word)

    # Remove word from Lexicon (return nothing)
    def remove(self, word):
        self.array.remove(word)

a = Lexicon()
print(a.__dict__)
a.insert('cat')
print(a)
print(a.__dict__)
print(a.find('cat'))
a.remove('cat')
print(a)
print(a.__dict__)