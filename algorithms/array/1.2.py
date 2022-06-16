answer = 'CORRECT'
string = input()
brackets = '()[]{}'
stack = []
for item in string:
    if item in brackets:
        stack.append(item)

pairs = {'(': ')',
         '[': ']',
         '{': '}'}

queue = []

for item in stack:
    if item in pairs:
        queue.append(item)
    elif item in pairs.values():
        if queue:
            if pairs.get(queue[-1], '') == item:
                queue.pop()
        else:
            answer = 'WRONG'
if queue:
    answer = 'WRONG'
print(answer)

