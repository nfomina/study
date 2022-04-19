from random import choice

with open('random.txt', 'w') as file:
    for _ in range(25):
        file.write(str(choice(range(111, 778))) + '\n')


# short
# from random import randrange
# with open('random.txt','w') as out:
#     print(*[randrange(111,778) for _ in range(25)],sep='\n',file=out)