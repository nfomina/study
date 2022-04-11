import random

string = [i for i in input()]
random.shuffle(string)
print(''.join(string))
