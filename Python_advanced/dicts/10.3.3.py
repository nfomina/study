text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}
for item in text:
    result[item] = result.get(item, 0) + 1

print(result)