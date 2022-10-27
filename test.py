import itertools
cases = []
for i in itertools.product('*+', repeat=8):
    cases.append(i)

for case in cases:
    a = 1
    sum_ = 1
    steps = 1
    for operation in case:
        if operation == '*':
            a = a * 2
        else:
            a += 1
        sum_ += a
        steps += 1
        if sum_ == 100:
            print(case, sum_, steps)
        elif sum_ > 100:
            break


