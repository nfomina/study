import sys
from datetime import datetime

data = [datetime.strptime(i.strip(), '%d.%m.%Y') for i in sys.stdin]

if len(data) == len(set(data)):
    if sorted(data) == data:
        print('ASC')
    elif sorted(data, reverse=True) == data:
        print('DESC')
    else:
        print('MIX')
else:
    print('MIX')



# shortly
# import sys
# from datetime import datetime, date
#
# dates = [datetime.strptime(line.strip(), '%d.%m.%Y') for line in sys.stdin]
#
# if sorted(list(set(dates))) == dates:
#     print('ASC')
# elif sorted(list(set(dates)), reverse=True) == dates:
#     print('DESC')
# else:
#     print('MIX')