
def same_parity(numbers):
    if numbers:
        if numbers[0] % 2 == 0:
            return [i for i in numbers if i % 2 == 0]
        else:
            return [i for i in numbers if i % 2 == 1]
    else:
        return []





print(same_parity([6, 0, 67, -7, 10, -20]))
print(same_parity([]))
print(same_parity([-7, 0, 67, -9, 70, -29, 90]))
print(same_parity([2]))
print(same_parity([2, 2, 2, 2, 3, 0, 2, 3]))
print(same_parity([-1, 1248234832443, 8]))
print(same_parity([1, 2, 4, 6, 8]))
print(same_parity([1, 3, 5, 7, 9]))

# wonderful
# def same_parity(nums):
#     return [i for i in nums if i % 2 == nums[0] % 2]