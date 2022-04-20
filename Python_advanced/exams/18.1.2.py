sum = 0
with open('ledger.txt') as file:
    lines = file.readlines()
    for line in lines:
        sum += int(line.replace('$', ''))

print(f'${sum}')