
symbols = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~1234567890'

input_string = input()
new_string = ''
for item in input_string:
    if item not in symbols:
        new_string += item
print(new_string)

# Sample Input 1:
#
# 1kilg%rli8k
# Sample Output 1:
#
# True
# Sample Input 2:
#
# kkkkkkkkkee
# Sample Output 2:
#
# False