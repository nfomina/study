
coords = [int(i) for i in input().split()]
colors = input().split()

matches = {}
for i, color in  enumerate(colors):
    if color in matches:
        matches[color].append(coords[i])
    else:
        matches[color] = [coords[i]]

max_distance = 0
for item in matches:
    if len(matches[item]) > 1:
        distance = max(matches[item]) - min(matches[item])
        if distance > max_distance:
            max_distance = distance


print(max_distance)






# Sample Input 1:
#
# 1 3 5 6 10 21 22
# r g b w w r g
# Sample Output 1:
#
# 20
# Sample Input 2:
#
# 1 2 3 4 5 6 7
# green blue b r white dark key
# Sample Output 2:
#
# 0
# Sample Input 3:
#
# 2 5 10 11 16 17 18 20
# r w g w g r w b
# Sample Output 3:
#
# 15