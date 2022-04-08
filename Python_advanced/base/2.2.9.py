string = input()

count = 0
max = 0

for item in string:
    if item == 'Р':
        count+=1
    else:
        if count > max:
            max = count
        count = 0
    if count > max:
        max = count
print(max)


# beautifull solution:
#
# s = input().split('О')
# print(len(max(s)))