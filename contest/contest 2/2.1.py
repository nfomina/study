n = int(input())
if n==1:
    print(1)
else:
    new_list = []
    i = 0
    last_element = 1
    while last_element < n+1:
        reverse_list = [t for t in range(last_element + i, last_element-1, -1)]
        new_list.extend(reverse_list)
        last_element += i+1
        i += 1
    print(*new_list[:n])

# Sample Input 1:
#
# 9
# Sample Output 1:
#
# 1 3 2 6 5 4 10 9 8
# Sample Input 2:
#
# 1
# Sample Output 2:
#
# 1
# Sample Input 3:
#
# 100
# Sample Output 3:
#
# 1 3 2 6 5 4 10 9 8 7 15 14 13 12 11 21 20 19 18 17 16 28 27 26 25 24 23 22 36 35 34 33 32 31 30 29 45 44 43 42 41 40 39 38 37 55 54 53 52 51 50 49 48 47 46 66 65 64 63 62 61 60 59 58 57 56 78 77 76 75 74 73 72 71 70 69 68 67 91 90 89 88 87 86 85 84 83 82 81 80 79 105 104 103 102 101 100 99 98 97