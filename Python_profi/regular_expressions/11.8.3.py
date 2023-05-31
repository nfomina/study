import keyword
import re


string = input().strip()
print(re.sub(r'\w*',
             lambda a: '<kw>' if a.group(0).lower() in [item.lower() for item in keyword.kwlist] else a.group(0),
             string))

# short
# import re
# import keyword
#
# keys = '|'.join(keyword.kwlist)
#
# print(re.sub(fr"\b({keys})\b", r'<kw>', input(), flags=re.I))
