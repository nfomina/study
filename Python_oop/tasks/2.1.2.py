string = input()

buffer = []
pairs = {')': '(',
         '}': '{',
         ']': '[',
         }
for item in string:
    if buffer:
        if pairs.get(item) == buffer[-1]:
            buffer.pop()
        else:
            buffer.append(item)
    else:
        buffer.append(item)
if not buffer:
    print('True')
else:
    print('False')
