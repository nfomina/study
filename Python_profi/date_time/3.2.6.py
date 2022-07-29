from datetime import date

n = int(input())
dates = []
for _ in range(n):
    dates.append(date.fromisoformat(input()))

for item in sorted(dates):
    print(item.strftime('%d/%m/%Y'))