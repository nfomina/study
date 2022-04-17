def pretty_print(data, side='-', delimiter='|'):
    string = delimiter, f' {delimiter} '.join(map(str, data)), delimiter
    count_delimeters = sum([len(str(i)) for i in data]) + len(data)*3 - 1
    print(' ', side * count_delimeters, sep='')
    print(*string)
    print(' ', side * count_delimeters, sep='')



pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')