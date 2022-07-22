
ru = "АаВСсЕеНКМОоРрТХху"
en = "AaBCcEeHKMOoPpTXxy"

letters = [input() for _ in range(3)]

res = [list(filter(lambda letter: letter in ru, letters)), list(filter(lambda letter: letter in en, letters))]

if res[0] and res[1]:
    print('mix')
elif res[0]:
    print('ru')
else:
    print('en')


# best
# langs = ['ru', 'mix', 'mix', 'en']
# eng = 'AaBCcEeHKMOoPpTXxy'
# ind = sum(input() in eng for _ in range(3))
# print(langs[ind])