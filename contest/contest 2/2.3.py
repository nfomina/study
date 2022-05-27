# n, m = [int(i) for i in input().split()]
#
# grandpa_distance = 0
#
# if abs(n) > abs(m):
#     first_runner = m
#     second_runner = n
# else:
#     first_runner = n
#     second_runner = m
# time = 0
# while grandpa_distance < abs(first_runner):
#     time += 1
#     if first_runner >= 0:
#         first_runner += 1
#     else:
#         first_runner -= 1
#     grandpa_distance +=2
# grandpa_point = first_runner
# if second_runner > 0:
#     second_runner += time
# else:
#     second_runner -= time
#
# if second_runner > grandpa_point:
#     while grandpa_point < second_runner:
#         if second_runner >= 0:
#             second_runner += 1
#         else:
#             second_runner -= 1
#         grandpa_distance += 2
#         grandpa_point += 2
# else:
#     while grandpa_point > second_runner:
#         if second_runner >= 0:
#             second_runner += 1
#         else:
#             second_runner -= 1
#         grandpa_distance += 2
#         grandpa_point -= 2
#
#
# print(grandpa_distance)

#
# Sample Input 1:
#
# 1 3
# Sample Output 1:
#
# 6
# Sample Input 2:
#
# -1 1
# Sample Output 2:
#
# 10
# Sample Input 3:
#
# -3 -6
# Sample Output 3:
#
# 12

n, m = [int(i) for i in input().split()]
if (n > 0 and m > 0) or (n < 0 and m < 0):
    print(2*max(abs(n), abs(m)))
else:
    s1 = 2*min(abs(n), abs(m))
    t1 = s1//2
    s2 = ((max(abs(n), abs(m))) + t1 + s1)*2
    print(s1 + s2)

