from collections import Counter


def print_bar_chart(data, mark):
    res = Counter(data)
    max_len = len(max(res, key=lambda a: len(a)))
    for key, count in sorted(res.items(), key=lambda a: a[1], reverse=True):
        print(f'{key} {" "*(max_len-len(key))}|{mark*count}')


print_bar_chart('beegeek', '+')

languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']

print_bar_chart(languages, '#')