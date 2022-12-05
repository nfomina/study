from collections import namedtuple
import pickle

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('data.pkl', 'rb') as f:
    animals = pickle.load(f)
# Person._make(['Timur', 29, 170])
for animal in animals:
    animal_ = Animal._make(animal)
    for field, value in zip(Animal._fields, animal_):
        print(f'{field}: {value}')
    print()


# short

# with open('data.pkl', 'rb') as animals_f:
#   for animal in pickle.load(animals_f):
#     print('name: {}\nfamily: {}\nsex: {}\ncolor: {}\n'.format(*animal))
