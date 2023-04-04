eval_string = eval(input())

if type(eval_string) is list:
    print(eval_string[-1])
elif type(eval_string) is tuple:
    print(eval_string[0])
else:
    print(len(eval_string))


# short
# n = eval(input())
# print(eval({list: 'n[-1]', tuple: 'n[0]', set: 'len(n)'}[type(n)]))
