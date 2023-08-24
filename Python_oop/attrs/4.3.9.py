class TextHandler:
    def __init__(self):
        self.words = []

    def add_words(self, text):
        self.words.extend(text.split())

    def get_shortest_words(self):
        if self.words:
            min_len = min([len(word) for word in self.words])
            return [word for word in self.words if len(word) == min_len]
        else:
            return []

    def get_longest_words(self):
        if self.words:
            max_len = max([len(word) for word in self.words])
            return [word for word in self.words if len(word) == max_len]
        else:
            return []


texthandler = TextHandler()

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())

texthandler = TextHandler()

texthandler.add_words('do not be sorry')
texthandler.add_words('be')
texthandler.add_words('better')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())

texthandler = TextHandler()

texthandler.add_words('The world will hold my trial for your sins')
texthandler.add_words('Never meant to see the sky, never meant to live')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())

# beauty
# class TextHandler:
#     def __init__(self):
#         self.words = []
#         self.shortest = 0
#         self.longest = 0
#
#     def add_words(self, words):
#         words = words.split()
#         self.words.extend(words)
#         self.shortest = min(map(len, self.words))
#         self.longest = max(map(len, self.words))
#
#     def get_shortest_words(self):
#         return [w for w in self.words if len(w) == self.shortest]
#
#     def get_longest_words(self):
#         return [w for w in self.words if len(w) == self.longest]
