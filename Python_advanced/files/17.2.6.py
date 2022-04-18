with open('prices.txt') as file:
    shop = file.readlines()

sum = 0
for item in shop:
    name, count, price = item.split('\t')
    sum += int(count) * int(price)

print(sum)