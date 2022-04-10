sentence = input().split()

dictionary = {}
for word in sentence:
    dictionary[word] = dictionary.get(word, 0) + 1
    print(dictionary.get(word), end = ' ')
