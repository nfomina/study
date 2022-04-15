is_num = lambda x: x.replace('.', '' ,1).isdigit() if not x.startswith('-') else x.replace('.', '' ,1).replace('-', '', 1).isdigit()


print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('-18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
print(is_num('--13.2'))
print(is_num('1-1'))

# short
# is_num = lambda x: x.lstrip("-").replace(".", "", 1).isdecimal()