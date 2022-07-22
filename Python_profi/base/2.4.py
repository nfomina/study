string = input().split()
res = set()
uniq = []
for item in string:
    if item in uniq:
        res.add(item)
    else:
        uniq.append(item)

print(*sorted(res))


# short
# nums = [int(i) for i in input().split()]
# print(*sorted(filter(lambda i: nums.count(i) > 1, set(nums))))