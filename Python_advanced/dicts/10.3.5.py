pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}
for item in pets:
    if (item[1], item[2], item[3]) in result:
        result[(item[1], item[2], item[3])].append(item[0])
    else:
        result[(item[1], item[2], item[3])] = [item[0]]
print(result)

# so easy
# for pet in pets:
#     result.setdefault(pet[1:], []).append(pet[0])