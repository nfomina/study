import sys


for line in sys.stdin:
    item = eval(line.strip())
    if -90 <= item[0] <= 90 and -180 <= item[1] <= 180:
        print('True')
    else:
        print('False')


# (75, 180)
# (90, -147.45)
# (77.111, 149.9999)
# (90, 180)
# (55.1, 249.9)
# (120, 150)