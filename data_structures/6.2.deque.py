import collections

class Lexicon:
    def __init__(self):
        self.linkedList = collections.deque()

    # Return True if Lexicon contains word, otherwise return False
    def find(self, word):
        if word in self.linkedList:
            return True
        return False

    # Insert word into Lexicon (return nothing)
    def insert(self, word):
        self.linkedList.append(word)

    # Remove word from Lexicon (return nothing)
    def remove(self, word):
        self.linkedList.remove(word)

a = Lexicon()
print(a.__dict__)
a.insert('cat')
print(a.__dict__)
print(a.find('cat'))
a.remove('cat')
print(a.__dict__)
print(a)

