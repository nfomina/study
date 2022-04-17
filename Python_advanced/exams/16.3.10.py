n = int(input())

words = []
for _ in range(n):
    words.append(input())

def gematry(word):
    res = 0
    for i in word:
        res += ord(i.upper()) - ord('A')
    return res

words = sorted(words)
for word in sorted(words, key=lambda x: gematry(x)):
    print(word)
