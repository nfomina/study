
def filter_anagrams(word, words):
    return [item for item in words if sorted(list(word)) == sorted(list(item))]

word = 'abba'
anagrams = ['aabb', 'abcd', 'bbaa', 'dada']

print(filter_anagrams(word, anagrams))

print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))
print(filter_anagrams('tommarvoloriddle', ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']))
print(filter_anagrams('стекло', []))
print(filter_anagrams('крона', ['кротко', 'укроп', 'норка']))
print(filter_anagrams('чулки', ['лучик', 'чутко', 'кочка']))
print(filter_anagrams('клоун', ['колдун', 'кулон', 'уклон', 'кол']))
word = 'abba'
anagrams = ['aaab', 'dbcd', 'bdaa', 'badb']
print(filter_anagrams(word, anagrams))