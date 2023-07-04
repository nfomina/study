from datetime import datetime

year = int(input())
month = int(input())
first_w = datetime(year, month, 1).isoweekday()
if first_w <= 4:
    day = 4 - first_w + 22
else:
    day = 4 - first_w + 29
print(datetime(year, month, day).strftime('%d.%m.%Y'))

# # TEST_1:
# 2012
# 3
#
# # TEST_2:
# 2015
# 2
#
# # TEST_3:
# 2018
# 6
#
# # TEST_4:
# 2020
# 1
#
# # TEST_5:
# 2015
# 8
#
# # TEST_6:
# 2015
# 9
#
# # TEST_7:
# 2015
# 10
#
# # TEST_8:
# 2016
# 1
#
# # TEST_9:
# 2016
# 2
#
# # TEST_10:
# 2000
# 11
#
# # TEST_11:
# 1990
# 12
#
# # TEST_12:
# 2022
# 9
