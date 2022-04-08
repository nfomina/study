n = int(input())

dictionary = {}
for _ in range(n):
    word1, word2 = input().split()
    dictionary[word1] = word2
    dictionary[word2] = word1

print(dictionary.get(input()))