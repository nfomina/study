def findPartiion(arr, n):
    Sum = 0

    for i in range(n):
        Sum += arr[i]
    if (Sum % 2 != 0):
        return 0
    part = [0] * ((Sum // 2) + 1)

    for i in range((Sum // 2) + 1):
        part[i] = 0

    for i in range(n):

        for j in range(Sum // 2, arr[i] - 1, -1):
            if (part[j - arr[i]] == 1 or j == arr[i]):
                part[j] = 1

    return part[Sum // 2]

numbers = [int(i) for i in input().split()]
n = len(numbers)

if sum(numbers) % 2 != 0:
    print('False')
elif findPartiion(numbers, n) == 1:
    print('True')
else:
    print('False')


# smart
# lst = sorted(map(int, list(input().split())), reverse=True)
# lst1, lst2 = [0], [0]
# for n in lst:
#     if sum(lst1) > sum(lst2):
#         lst2.append(n)
#     else:
#         lst1.append(n)
#
# print(sum(lst1) == sum(lst2))