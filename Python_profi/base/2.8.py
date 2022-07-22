import re
workers = {}

def get_available(list_booked):
    for i in range(0, len(list_booked)+1):
        if i not in list_booked:
            return i

for _ in range(int(input())):
    name, tail = input().split('@')
    args = re.split('(\d+)', name)
    if len(args) > 1:
        if workers.get(args[0]):
            workers[args[0]].append(int(args[1]))
        else:
            workers[args[0]]= [int(args[1])]
    else:
        if workers.get(args[0]):
            workers[args[0]].append(0)
        else:
            workers[args[0]] = [0]


for _ in range(int(input())):
    name = input()
    if name in workers:
        next = get_available(workers[name])
        workers[name].append(next)
        if next == 0:
            next = ''
        print(f'{name}{next}@beegeek.bzz')
    else:
        print(f'{name}@beegeek.bzz')
        workers[name] = [0]

# such beaty
# digits, names = '0123456789', []
#
# for _ in range(int(input())):
#     name, _ = input().split('@')
#     names.append(name)
#
# for _ in range(int(input())):
#     name = input()
#     counter = 1
#     while name in names:
#         name = name.rstrip(digits) + str(counter)
#         counter += 1
#     names.append(name)
#     print(f'{name}@beegeek.bzz')