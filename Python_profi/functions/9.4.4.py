def remove_marks(text, marks):
    remove_marks.__dict__.setdefault('count', 0)
    remove_marks.count += 1
    for symbol in text:
        if symbol in marks:
            text = text.replace(symbol, '')
    return text

# text = 'Hi! Will we go together?'
#
# print(remove_marks(text, '!?'))
# print(remove_marks.count)

marks = '.,!?'
text = 'Are you listening? Meet my family! There are my parents, my brother and me.'

for mark in marks:
    print(remove_marks(text, mark))

print(remove_marks.count)

# def remove_marks(text, marks):
#     remove_marks.__dict__['count'] = remove_marks.__dict__.get('count', 0) + 1
#     for i in marks:
#         text = text.replace(i, '')
#     return text
