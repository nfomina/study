import re
import sys


page = '''<p><a href="https://stepik.org">Stepik</a></p>
<div class="catalog"><a href="https://stepik.org/catalog">Study hard. Teach harder</a></div>'''
res = {}
for line in sys.stdin:
    open_tags = re.findall('<[^/>][^>]*>', line)
    for tag in open_tags:
        tag_name = re.findall('<(\w*)', tag)[0]
        parse_attributes = re.findall('''(\S+)=["']?((?:.(?!["']?\s+(?:\S+)=|[>"']))+.)["']?''', tag)
        attributes = [i[0] for i in parse_attributes]
        if res.get(tag_name):
            for attr in attributes:
                res[tag_name].add(attr)
        else:
            res[tag_name] = set(attributes)
for tag in sorted(res):
    print(f'{tag}: {", ".join(sorted(res[tag]))}')


# best
# import re
#
# res = {}
# for line in open(0):
#     for tag, params in re.findall(r'<(\w+)(.*?)>', line):
#         res.setdefault(tag, set()).update(re.findall(r'([\w-]+)=', params))
#
# for key in sorted(res):
#     print(f'{key}: {", ".join(sorted(res[key]))}')
