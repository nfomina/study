class Pet:
    pets = []

    def __init__(self, name):
        self.name = name
        __class__.pets.append(self)

    @classmethod
    def first_pet(cls):
        if __class__.pets:
            return __class__.pets[0]
        else:
            cls.name = None

    @classmethod
    def last_pet(cls):
        if __class__.pets:
            return __class__.pets[-1]
        else:
            cls.name = None

    @classmethod
    def num_of_pets(cls):
        return len(__class__.pets)


print(Pet.first_pet())
print(Pet.last_pet())
print(Pet.num_of_pets())

pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())

# TEST_3:
names = ['Mia', 'Tutti', 'Erin', 'Loki', 'Kelly', 'Hussy', 'Abbey', 'Luna', 'Isha', 'Diva', 'Brandy', 'Petra', 'Mandy', 'Baby', 'Caitlyn', 'Taffy', 'Odie', 'Roxxy', 'Gabby', 'Shelby', 'Dolly', 'Ashley', 'Vanilla', 'Cori']

for name in names:
    pet = Pet(name)

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())

# TEST_4:
pet = Pet('Кемаль')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())

# TEST_5:
pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')
pet4 = Pet('Ratchet')
pet5 = Pet('Ratchet')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())
