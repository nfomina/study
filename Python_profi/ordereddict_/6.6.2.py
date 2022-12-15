from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                    'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
                    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})
new_data = []

flag = True
while data:
    flag = not flag
    new_data.append(data.popitem(last=flag))

print(OrderedDict(new_data))

# shortly
# data = OrderedDict([data.popitem(last=i & 1) for i in range(len(data))])
