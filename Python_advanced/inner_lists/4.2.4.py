list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]

list1 = [elem[::-1] for elem in list1]
print(list1)

res = [[8, 7, 1], [102, 7, 9], [105, 106, 102], [103, 98, 99, 100], [3, 2, 1]]

print(res==list1)

# beautiful:
# [x.reverse() for x in list1]