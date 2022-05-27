def get_all_divisors_brute(n):
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            yield i
    yield n

string = input()
len_string = len(string)

divisors = get_all_divisors_brute(len(string))
for divisor in divisors:
    count_substring = string.count(string[0:divisor])
    if len_string == count_substring*divisor:
        print(count_substring)
        break



# Sample Input 1:
# abcabcabc
# Sample Output 1:
# 3
# Sample Input 2:
# acdc
# Sample Output 2:
# 1
# Sample Input 3:
# bbbbbb
# Sample Output 3:
# 6
# Sample Input 4:
# abobaboabobabo
# Sample Output 4:
# 2
# Sample Input 5:
# abobaboaaabobaboaa
# Sample Output 5:
# 2
# Sample Input 6:
# bebebeb
# Sample Output 6:
# 1