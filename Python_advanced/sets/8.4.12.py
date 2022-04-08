words = [word.lower() for word in input().split()]
new_set = set()
for word in words:
    for junk_char in ".,;:-?!": word = word.replace(junk_char, '')
    new_set.add(word)

print(len(new_set))

# short
# words = [word.lower().strip('.,;:-?!') for word in input().split()]
#
# print(len(set(words)))