code = input()

start_item = code[0]
for item in code:
    if item == '|':
        pass
    elif item == start_item:
        print(0, end='')
    else:
        print(1, end='')
        start_item = item



# Sample Input 1:
#
# _|¯|____|¯|__|¯¯¯
# Sample Output 1:
#
# 011000110100