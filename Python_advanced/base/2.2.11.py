word = input()

base = "запретил букву"
sentence = word + ' ' + base
letters = sorted(set(filter(str.isalpha, sentence)))

for alpha in letters:
    print(sentence + ' ' + alpha)
    sentence = sentence.replace(alpha, '')
    sentence = " ".join(sentence.split())