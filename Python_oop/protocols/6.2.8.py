class HistoryDict:
    def __init__(self, data={}):
        self._items = dict(data) or {}
        self._history = {k: [v] for k, v in self._items.items()}

    def __getitem__(self, item):
        return self._items[item]

    def __getattr__(self, item):
        return self._items[item]

    def __setitem__(self, key, value):
        self._items[key] = value
        self._history.setdefault(key, []).append(value)

    def __iter__(self):
        yield from self._items

    def __len__(self):
        return len(self._items)

    def keys(self):
        yield from self._items.keys()

    def values(self):
        yield from self._items.values()

    def items(self):
        yield from self._items.items()

    def __delitem__(self, key):
        del self._items[key]
        del self._history[key]

    def history(self, key):
        return self._history.get(key, [])

    def all_history(self):
        return self._history


historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(historydict['ducks'])
print(historydict['cats'])
print(len(historydict))

historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(*historydict)
print(*historydict.keys())
print(*historydict.values())
print(*historydict.items())

historydict = HistoryDict({'ducks': 99, 'cats': 1})

historydict['ducks'] = 100
print(historydict.history('ducks'))
print(historydict.history('cats'))
print(historydict.history('dogs'))

historydict = HistoryDict({'ducks': 99, 'cats': 1})

print(historydict.all_history())
historydict['ducks'] = 100
historydict['ducks'] = 101
historydict['cats'] = 2
print(historydict.all_history())

historydict = HistoryDict({'ducks': 99, 'cats': 1})

historydict['dogs'] = 1
print(len(historydict))
del historydict['ducks']
del historydict['cats']
print(len(historydict))

# TEST_6:
d = {'name': 'Иннокентий Елисеевич Архипов', 'age': 34, 'year': 1989}
historydict = HistoryDict(d)

names = ['Регина Ефимовна Костина', 'Мина Викторович Лаврентьев', 'Голубева Юлия Робертовна',
         'Чернова Варвара Максимовна', 'Юдин Матвей Иосипович', 'Степанов Мечислав Ерофеевич',
         'Абрамов Амос Августович', 'Ольга Егоровна Константинова', 'Хохлов Ираклий Ефимьевич',
         'Нестеров Никон Ермилович', 'Третьякова София Юльевна', 'Кудряшова Нина Юльевна', 'Казакова Раиса Феликсовна',
         'Александрова Надежда Николаевна', 'Никон Давыдович Васильев', 'Пахом Ильясович Морозов',
         'Дмитрий Тихонович Панов', 'Лебедева Галина Валериевна', 'Кузьмина Анастасия Викторовна',
         'Севастьян Жанович Якушев']

ages = [37, 20, 31, 21, 38, 24, 31, 24, 37, 20, 22, 39, 25, 21, 28, 28, 30, 30, 36, 23]

years = [1986, 2003, 1992, 2002, 1985, 1999, 1992, 1999, 1986, 2003, 2001, 1984, 1998, 2002, 1995, 1995, 1993, 1993,
         1987, 2000]

for name, age, year in zip(names, ages, years):
    historydict['name'] = name
    historydict['age'] = age
    historydict['year'] = year

print(*historydict.items())
print(historydict.history('name'))
print(historydict.history('age'))
print(historydict.history('year'))

# TEST_7:
historydict = HistoryDict()
print('Keys:', *historydict.keys())
print('Values:', *historydict.values())
print('Items:', *historydict.items())
print('History(key=1):', historydict.history(1))
print('History(key=1):', historydict.history(1))
print('All history:', historydict.all_history())

# TEST_8:
historydict = HistoryDict({'name': 'Irenica', 'country': 'Russia', 'level': 'junior', })

print(historydict.all_history())

historydict['country'] = 'Italy'
historydict['level'] = 'middle'
historydict['level'] = 'senior'

print(historydict.all_history())

del historydict['level']

print(historydict.all_history())

historydict['level'] = 'God'

print(historydict.all_history())

# TEST_9:
d = dict.fromkeys(range(100), None)
attrdict = HistoryDict(d)
print(*attrdict)

d[100] = None
print(*attrdict)
