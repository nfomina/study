class DevelopmentTeam:
    def __init__(self):
        self.juniors = []
        self.seniors = []

    def add_junior(self, *args):
        for arg in args:
            self.juniors.append((arg, 'junior'))

    def add_senior(self, *args):
        for arg in args:
            self.seniors.append((arg, 'senior'))

    def __iter__(self):
        yield from iter(self.juniors)
        yield from iter(self.seniors)

beegeek = DevelopmentTeam()

beegeek.add_junior('Timur')
beegeek.add_junior('Arthur', 'Valery')
beegeek.add_senior('Gvido')
print(*beegeek, sep='\n')

beegeek = DevelopmentTeam()

print(len(list(beegeek)))

beegeek = DevelopmentTeam()

beegeek.add_junior('Timur')
beegeek.add_junior('Arthur', 'Valery')
print(*beegeek, sep='\n')

# TEST_4:
beegeek = DevelopmentTeam()

beegeek.add_senior('Arthur', 'Valery', 'Timur')
print(*beegeek, sep='\n')

# TEST_5:
smart_monkey = DevelopmentTeam()

smart_monkey.add_senior('Gvido', 'Alan')
smart_monkey.add_junior('Denis')

print(list(smart_monkey))

# TEST_6:
pied_piper = DevelopmentTeam()

pied_piper.add_senior('Richard', 'Gilfoyle', 'Dinesh', 'Erlich')
pied_piper.add_junior('Jared', 'Big Head')

print(*pied_piper, sep='\n')
print(len(list(pied_piper)))
