class Node:
    def __init__(self):
        self.is_word = False
        self.children = {}


class MultiwayTrie:
    def __init__(self):
        self.root = Node()

    # Return True if Lexicon contains word, otherwise return False
    def find(self, word):
        node = self.root
        for char in word:
            # char = ord(char.lower()) - 97
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node.is_word

    def insert(self, word):
        node = self.root
        for char in word:
            # char = ord(char.lower()) - 97
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_word = True

    # Remove word from Lexicon (return nothing)
    def remove(self, word):
        node = self.root
        for char in word:
            # letter = ord(char.lower()) - 97
            if node.children[char]:
                node = node.children[char]
        if node.is_word:
            node.is_word = False


test = MultiwayTrie()
test.insert('INSERT')
test.insert('ac')
test.insert('gram')
# print(test.root.children)
# print(test.root.children[0].children)
# print(test.root.children[0].children[2].is_word)
print(test.find('INSERT'))
print(test.find('ac'))
print(test.find('gram'))

test.remove('ac')

print(test.find('ac'))
print(test.find('abtest'))
print(test.root.children)



# etalon
#
# class Node:
#     def __init__(self):
#         self.is_word = False
#         self.children = [None] * 26
#
#
# class MultiwayTrie:
#     def __init__(self):
#         self.root = Node()
#
#     # Return True if Lexicon contains word, otherwise return False
#     def find(self, word):
#         # YOUR CODE HERE
#         curr = self.root
#         for ch in word:
#             if curr.children[ord(ch) - ord('A')] is None:
#                 return False
#             else:
#                 curr = curr.children[ord(ch) - ord('A')]
#         return curr.is_word
#
#     # Insert word into Lexicon (return nothing)
#     def insert(self, word):
#         # YOUR CODE HERE
#         curr = self.root
#         for ch in word:
#             if curr.children[ord(ch) - ord('A')] is None:
#                 curr.children[ord(ch) - ord('A')] = Node()
#                 curr = curr.children[ord(ch) - ord('A')]
#         curr.is_word = True
#
#     # Remove word from Lexicon (return nothing)
#     def remove(self, word):
#         # YOUR CODE HERE
#         curr = self.root
#         for ch in word:
#             if curr.children[ord(ch) - ord('A')] is None:
#                 return
#             else:
#                 curr = curr.children[ord(ch) - ord('A')]
#         curr.is_word = False