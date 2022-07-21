
def index_of_nearest(numbers, number):
    distance = [abs(item-number) for item in numbers]
    if distance:
        return  distance.index(min(distance))
    return -1

print(index_of_nearest([], 17))
print(index_of_nearest([7, 13, 3, 5, 18], 0))
print(index_of_nearest([9, 5, 3, 2, 11], 4))
print(index_of_nearest([7, 5, 4, 4, 3], 4))
print(index_of_nearest([6, 100, 101, 2], 4))
print(index_of_nearest([734234423423423, 5343423423546463423, 934234423423423423, -1], 0))
print(index_of_nearest([1, 14, 100, 65, 6], 5))
print(index_of_nearest([10, 164, 100, 265, 16], 8))
print(index_of_nearest([10, 99, 0, -12, 16], -9))
print(index_of_nearest([1, 1, 1, 1, 1], 1))

# with lambda

# def index_of_nearest(nums, n):
#     if nums:
#         minimum = min(nums, key=lambda num: abs(num - n))
#         return nums.index(minimum)
#     return -1