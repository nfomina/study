with open('nums.txt') as file:
    sum_ = 0
    line = file.readline()
    while line != '':
        for i in line:
            if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                line = line.replace(i, ' ')
        sum_ += sum(map(int, line.split()))
        line = file.readline()

print(sum_)

#  smart
# with open('numbers.txt', encoding='utf-8') as file:
#     row = ''.join(c if c.isdigit() else ' ' for c in file.read())
#     print(sum(map(int, row.split())))