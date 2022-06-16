import operator

OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}


def polska(srt):
    stack = []
    lst = srt.split()
    for i in srt.split():
        if i.isdigit():
            stack.append(i)
            lst.remove(i)
        else:
            cnt1, cnt2 = stack.pop(), stack.pop()
            stack.append(OPERATORS[i](int(cnt2), int(cnt1)))
            lst.remove(i)
    return stack.pop()

print(polska(input()))