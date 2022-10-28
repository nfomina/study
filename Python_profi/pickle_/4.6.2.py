import pickle
import sys

f = open(input(), 'rb')
fnc = pickle.load(f)
f.close()

print(fnc(*list(map(str.strip, sys.stdin))))
