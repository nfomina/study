# put your python code here
n = int(input())


def count_number(n):
    res = 9
    number = 9
    i = 1
    while n > res:
        res += 9*pow(10, i)*(i+1)
        number += 9 * pow(10, i)
        i += 1
    i -= 1
    res -= 9*pow(10, i)*(i+1)
    number -= 9 * pow(10, i)
    if res+1 == n:
        return str(res+1)[-1][0]
    needed_number = (n-res)//(i+1)
    position = (n-res) % (i+1)
    number += needed_number
    if position == 0:
        return str(number)[0]
    number = str(number+1)[::-1]
    return number[position-1]


if n > 9:
    print(count_number(n))
else:
    print(n)



