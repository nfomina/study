import re
string = input()
new_string = string.replace('(', '*(')
new_string = new_string.replace(')', ')+')
line = re.findall('\d+', new_string)
for item in line:
    new_string = new_string.replace(item, f'+{item}')

line = re.findall('[a-z]{1,}', new_string)
new_eval_string = ''
flag = 0
for i in new_string:
    if i.isalpha() and flag == 0:
        flag = 1
        new_eval_string += f'\'{i}'
    elif i.isalpha() and flag == 1:
        new_eval_string += f'{i}'
    elif i.isalpha() is False and flag == 0:
        new_eval_string += f'{i}'
    else:
        flag = 0
        new_eval_string += f'\'{i}'

new_eval_string = new_eval_string.replace('(+', '(')
result_string = ''
separate_plus = new_eval_string.split('+')

for item in separate_plus:
    if item and item != ')':
        if result_string:
            result_string += '+' + item
        else:
            result_string = item
    elif item and item == ')':
        result_string += ')'


if result_string[-1].isalpha():
    result_string += '\''

print(eval(result_string))

# hi2(priv3(d3(i)dd)qq)b0(pr)qwqdd
# print('hi'+2*('priv'+3*('d'+3*('i')+'dd')+'qq')+'b'+0*('pr')+'qwqdd')


# Sample Input 1:
# hello3(world)hi
# Sample Output 1:
# helloworldworldworldhi
# Sample Input 2:
# 0(s)he0(be)lie0(ve)d
# Sample Output 2:
# helied
# Sample Input 3:
# bbbb10(2(a))bbb
# Sample Output 3:
# bbbbaaaaaaaaaaaaaaaaaaaabbb
# Sample Input 4:
# hi2(priv3(d3(i)dd)qq)b0(pr)qwqdd
# Sample Output 4:
# hiprivdiiidddiiidddiiiddqqprivdiiidddiiidddiiiddqqbqwqdd
# Sample Input 5:
# hhhhhh
# Sample Output 5:
# hhhhhh


# Best solution

string = input()
stack = []
result = ''
count_str = ''
a = 0
for i in range(len(string)):
    if string[i].isdigit():
        a = a * 10 + int(string[i])
        if string[i+1] == '(':
            if len(stack) >= 1 and type(stack[-1]) == str:
                stack[-1] += count_str
            else:
                stack.append(count_str)
            count_str = ''
    else:
        if string[i] == '(':
            stack.append(a)
        elif string[i] == ')':
            if type(stack[-1]) == int:
                stack[-2] = stack[-2] + count_str * stack[-1]
                stack.pop()
            else:
                stack[-3] = stack[-3] + (stack[-1] + count_str) * stack[-2]
                stack.pop()
                stack.pop()
            count_str = ''
        else:
            count_str += string[i]
        a = 0
if (len(stack) == 0):
    print(count_str)
else:
    print(stack[-1] + count_str)