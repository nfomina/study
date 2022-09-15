import sys
news = {}
for x in sys.stdin:
    try:
        text, theme, quality = x.split(' / ')
        if news.get(theme):
            news[theme].append((text, quality[:-1]))
        else:
            news[theme] = [(text, quality[:-1])]
    except:
        theme = x[:-1]

for item in sorted(news[theme], key=lambda tup: (tup[1], tup[0])):
    print(item[0])

# beauty

# import sys
#
# *news, tag = [line.strip().split(' / ') for line in sys.stdin]
# true_news = [n for n in news if n[1] == tag[0]]
#
# for n in sorted(true_news, key=lambda x: (float(x[2]), x[0])):
#     print(n[0])