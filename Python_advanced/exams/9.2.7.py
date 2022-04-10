m = int(input())
n = int(input())

maths = set()
for _ in range(m):
    maths.add(input())
infos = set()
for _ in range(n):
    infos.add(input())

print(len(maths-infos))
