class RandomLooper:
    def __init__(self, *args):
        self.items = []
        for arg in args:
            self.items.extend(arg)
        self.iter_items = iter(self.items)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.iter_items)


randomlooper = RandomLooper(['red', 'blue', 'green', 'purple'])

print(list(randomlooper))
print(list(randomlooper))

# TEST_2:
colors = ['red', 'blue', 'green', 'purple']
shapes = ['square', 'circle', 'triangle', 'octagon']
randomlooper = RandomLooper(colors, shapes)

print(list(randomlooper))

# TEST_3:
from string import ascii_letters

domains = ['huynh.biz', 'riley.net', 'herman.org', 'tran-guerrero.com', 'martinez.com', 'riley-moore.info', 'allen.com',
           'lopez.com', 'santiago.com', 'moran-craig.com', 'smith-graves.com', 'smith.com', 'johnson.biz',
           'gregory-smith.com', 'smith.com', 'douglas.com', 'marshall.com', 'henry-garcia.com', 'gardner.biz',
           'allen.com']

work = {'Public librarian', 'Horticulturist, commercial', 'Archaeologist', 'Neurosurgeon', 'Investment analyst',
        'Energy manager', 'Conservation officer, historic buildings', 'Town planner',
        'Research scientist (physical sciences)', 'Dancer', 'Financial adviser', 'Human resources officer',
        'Meteorologist', 'Water quality scientist', 'Call centre manager', 'Surveyor, rural practice',
        'Sports administrator', 'Electronics engineer', 'Pharmacist, hospital', 'Local government officer'}

phone_numbers = ('934.394.1303x57945', '178-222-6477x229', '+1-656-770-5470x078', '+1-297-950-6100',
                 '(931)443-0778x87575', '329-788-0662', '+1-955-232-3577x6474', '001-562-654-3195x083', '854.344.9086',
                 '546-622-8169', '(161)097-6037', '(539)319-3442', '001-874-988-4679x3997', '079-860-8803x913',
                 '2410563363', '(852)061-7986x980', '393.485.5132', '+1-089-015-3223x3791', '(010)648-5657x225',
                 '497.913.4838x8085')

names = {'Frank Oconnor': 'FO', 'Brittany Mccoy': 'BM', 'Ariana Jackson': 'AJ', 'Jeffrey Smith': 'JS',
         'Oscar Gay': 'OG', 'Eric Hanson': 'EH', 'Anthony Robinson': 'AR', 'Ricky Garcia': 'RG', 'Derrick Cruz': 'DC',
         'Brittany Simpson': 'BS', 'Richard Tran': 'RT', 'Denise Hernandez': 'DH', 'Michael Lin': 'ML',
         'James James': 'JJ', 'Jacob Saunders': 'JS', 'Stephanie Sherman': 'SS', 'John Austin': 'JA',
         'Benjamin Mason': 'BM', 'Corey Brown': 'CB', 'Gregory Adams': 'GA'}

randomlooper = RandomLooper(domains, work, phone_numbers, names, ascii_letters)
print(list(randomlooper))

# TEST_4:
randomlooper = RandomLooper(['red', 'blue', 'green', 'purple'])

answer = [next(randomlooper) for _ in range(4)]
print(answer)
