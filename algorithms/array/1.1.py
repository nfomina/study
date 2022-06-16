def sum_numbers(filename):
    sum_ = 0
    with open(filename) as f:
        while True:
            line = f.readline()
            if not line:
                break
            sum_ += int(line)
    return sum_

print(sum_numbers('test'))
