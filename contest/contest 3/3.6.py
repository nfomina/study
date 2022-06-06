from itertools import combinations

numbers = [int(i) for i in input().split()]

def difference(sublist1, sublist2):
    return abs(sum(sublist1) - sum(sublist2))

def complement(sublist, my_list):
    complement = my_list[:]
    for x in sublist:
        complement.remove(x)
    return complement

def divide(my_list):
    lower_difference = sum(my_list) + 1
    for i in range(1, int(len(my_list)/2)+1):
        for partition in combinations(my_list, i):
            partition = list(partition)
            remainder = complement(partition, my_list)

            diff = difference(partition, remainder)
            if diff < lower_difference:
                lower_difference = diff
                solution = [partition, remainder]

    return solution

if sum(numbers) % 2 != 0:
    print('False')
else:
    result = divide(numbers)
    if sum(result[0]) == sum(result[1]):
        print('True')
    else:
        print('False')
