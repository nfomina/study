string = input()

not_pair = []
count = 0
for item in string:
    if item in not_pair:
        count += 1
        not_pair.remove(item)
    else:
        not_pair.append(item)
if count*2 < len(string):
    print(count * 2 + 1)
else:
    print(count*2)


# Sample Input 1:
# ababqtd
# Sample Output 1:
# 5
# Sample Input 2:
# bebebe
# Sample Output 2:
# 5
# Sample Input 3:
# qaaaaaaaab
# Sample Output 3:
# 9