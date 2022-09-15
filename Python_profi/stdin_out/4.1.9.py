import sys

numbers = [int(i) for i in sys.stdin]

def check_geometric_progression(arr):
    l = len(arr)
    common_ratio = arr[1]/arr[0]
    for i in range(2, l):
        if arr[i]/arr[i - 1] != common_ratio:
            return False
    return True

def check_arithmetic_progression(arr):
    diff = arr[1] - arr[0]
    n = len(arr)
    for i in range(2, n):
        if arr[i] - arr[i - 1] != diff:
            return False
    return True

if len(numbers) > 1 and check_arithmetic_progression(numbers):
    print('Арифметическая прогрессия')
elif len(numbers) > 1 and check_geometric_progression(numbers):
    print('Геометрическая прогрессия')
else:
    print('Не прогрессия')