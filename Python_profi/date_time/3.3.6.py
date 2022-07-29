from datetime import datetime

with open('diary.txt', encoding='utf-8') as f:
    file = f.read()

records = file.split('\n\n')

print(*sorted(records, key=lambda record: datetime.strptime(record.split('\n')[0], '%d.%m.%Y; %H:%M')), sep='\n\n')
