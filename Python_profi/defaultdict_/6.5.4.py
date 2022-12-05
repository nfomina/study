from collections import defaultdict


def wins(pairs):
    result = defaultdict(set)
    for item in pairs:
        result[item[0]].add(item[1])
    return result


result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'), ('Артур', 'Анри'), ('Артур', 'Дима')])

for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))


# some beauty
# def wins(pairs):
#     result = defaultdict(set)
#     for winner, loser in pairs:
#         result[winner].add(loser)
#     return result
