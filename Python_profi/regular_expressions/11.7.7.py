import re
import sys


for line in sys.stdin:
    link = re.findall('\<a(.*)\</a\>', line.strip())
    for item in link:
        url = re.findall('href="(.*)"', item)
        other = re.findall('\>(.*)', item)
        print(''.join(url), ''.join(other), sep=', ')


# beauty
# text = sys.stdin.read()
# pattern = r'<a href="(.+)">(.+)</a>'
#
# for address, pointer in re.findall(pattern, text):
#     print(f'{address}, {pointer}')
