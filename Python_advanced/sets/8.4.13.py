numbers = [int(i) for i in input().split()]

uniq_elements = set()
for item in numbers:
    if item in uniq_elements:
        print('YES')
    else:
        uniq_elements.add(item)
        print('NO')