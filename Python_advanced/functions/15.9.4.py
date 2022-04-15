print(all(map(lambda x: x.isdigit() and int(x) in range(0, 256), input().split('.'))))
