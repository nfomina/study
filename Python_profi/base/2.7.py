template = input()
ru = 'ауоыиэяюёе'

def create_mask(template):
    for item in template:
        if item in ru:
            template = template.replace(item, '*', 1)
        else:
            template = template.replace(item, '#', 1)
    return template[:template.rfind('*')+1]

template = create_mask(template)

for _ in range(int(input())):
    word = input()
    mask_word = create_mask(word)
    if mask_word.startswith(template) and (len(mask_word) <= len(template) or '*' not in mask_word[len(template):]):
        print(word)


#  beauty
# vowels = ('а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')
# pattern = [i for i, c in enumerate(input()) if c in vowels]
#
# for _ in range(int(input())):
#     word = input()
#     if [i for i, c in enumerate(word) if c in vowels] == pattern:
#         print(word)