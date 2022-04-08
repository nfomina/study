elements = input().split()

count = 0
previous = int(elements[0])
for element in elements:
    if int(element) > previous:
        count += 1
    previous = int(element)
print(count)