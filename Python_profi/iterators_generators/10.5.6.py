def card_deck(suit):
    card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]
    card_mast = ["пик", "треф", "бубен", "червей"]
    card_mast.remove(suit)
    while True:
        for i in range(len(card_mast)):
            for j in range(len(card_values)):
                yield f'{card_values[j]} {card_mast[i]}'


generator = card_deck('пик')

print(next(generator))
print(next(generator))
print(next(generator))

generator = card_deck('треф')
cards = [next(generator) for _ in range(40)]

print(*cards)
