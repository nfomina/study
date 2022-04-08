s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'

result = {}
for item in s.split():
    result[item] = result.get(item, 0) + 1

top_numbers = sorted(result.items(), key = lambda k: k[1], reverse = True)[0][1]
top_words = {k:v for k, v in result.items() if v == top_numbers}
print(sorted(top_words)[0])

# pretty good
# d = {}
# for w in s.split():
#     d[w] = d.get(w, 0) + 1
# print(min(d, key=lambda x: (-d[x], x)))