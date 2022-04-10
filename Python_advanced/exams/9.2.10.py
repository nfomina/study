m = int(input())
n = int(input())

one_subject = set()
for _ in range(m+n):
    pupil = input()
    if pupil not in one_subject:
        one_subject.add(pupil)
    else:
        one_subject.remove(pupil)

if one_subject:
    print(len(one_subject))
else:
    print('NO')
