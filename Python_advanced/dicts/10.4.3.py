d = {}
for c in ''.join( c for c in input().lower() if  c not in '.,!?:;- ' ):
    d[c] = d.get(c, 0) + 1
for c in ''.join( c for c in input().lower() if  c not in '.,!?:;- ' ):
    d[c] = d.get(c, 0) - 1
print(('NO', 'YES')[set(d.values()) == {0}])

