import copy

def get_min_max(iterable):
    if iterable:
        copy_iter = copy.deepcopy(iterable)
        try:
            return min(iterable), max(copy_iter)
        except:
            return None


iterable = iter(range(10))

print(get_min_max(iterable))

# TEST_11:
data = iter(range(100_000_000))

print(get_min_max(data))
