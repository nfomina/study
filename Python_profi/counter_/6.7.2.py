from collections import Counter

def count_occurences(word, words):
    return Counter([w.lower() for w in words.split()])[word.lower()]


word = 'python'
words = 'Python Conferences python training python events'

print(count_occurences(word, words))
word = 'Java'
words = 'Python C++ C# JavaScript Go Assembler'

print(count_occurences(word, words))