import pickle

with open(input(), 'rb') as file:
    a = pickle.load(file)
check_sum = int(input())
sum_ = 0

if type(a) is list:
    new_list = list(filter(lambda x: type(x) == int, a))
    if new_list:
        sum_ = min(new_list) * max(new_list)
elif type(a) is dict:
    for item in a:
        if type(item) is int:
            sum_ += item

if sum_ == check_sum:
    print('Контрольные суммы совпадают')
else:
    print('Контрольные суммы не совпадают')

# smart
# import pickle
#
# name, sm = input(), int(input())
# with open(name, 'rb') as f:
#     obj = pickle.load(f)
#     lst = [i for i in obj if type(i) == int] or [0]
#     check = sum(lst) if type(obj) == dict else max(lst)*min(lst)
#     print(['Контрольные суммы не совпадают', 'Контрольные суммы совпадают'][sm == check])