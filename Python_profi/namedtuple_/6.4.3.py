import csv
from operator import attrgetter
from datetime import datetime
from collections import namedtuple

Person = namedtuple('Person', ['surname', 'name', 'meeting_date', 'meeting_time'])

with open('meetings.csv') as f:
    reader = csv.reader(f)
    next(reader)
    data = list(reader)

new_data = []
for item in data:
    new_item = Person._make([item[0], item[1], datetime.strptime(item[2], '%d.%m.%Y'),
                             datetime.strptime(item[3], '%H:%M')])
    new_data.append(new_item)

for item in sorted(new_data, key=lambda x: (x.meeting_date, x.meeting_time)):
    print(item.surname, item.name)

# smart enough

# import csv
#
# from collections import namedtuple
# from datetime import datetime
#
# convector = '%d.%m.%Y %H:%M'
# Friend = namedtuple('Friend', ['name_surname', 'datetime'])
# friends = []
#
# with open('meetings.csv', 'r', encoding='utf-8') as f:
#     header, *data = csv.reader(f)
#
# for d in data:
#     friends.append(Friend(f'{d[0]} {d[1]}', datetime.strptime(f'{d[2]} {d[3]}', convector)))
#
# for friend in sorted(friends, key=lambda f: f.datetime):
#     print(friend.name_surname)
