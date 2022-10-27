import json

with open("pools.json", encoding='UTF-8') as f:
    pools = json.loads(f.read())
    max_length = 0
    max_width = 0
    address = ''
    for pool in pools:
        working_hours_start, working_hours_end = pool['WorkingHoursSummer']['Понедельник'].split('-')
        if int(working_hours_start.split(':')[0]) <= 10 and int(working_hours_end.split(':')[0]) >= 12:
            if pool['DimensionsSummer']['Length'] > max_length:
                max_length = pool['DimensionsSummer']['Length']
                max_width = pool['DimensionsSummer']['Width']
                address = pool['Address']
            elif pool['DimensionsSummer']['Length'] == max_length:
                if pool['DimensionsSummer']['Width'] > max_width:
                    max_length = pool['DimensionsSummer']['Length']
                    max_width = pool['DimensionsSummer']['Width']
                    address = pool['Address']
print(f'{max_length}x{max_width}')
print(address)

# beauty
# import json
#
# with open('pools.json', encoding='utf8') as fi:
# 	tm = lambda x: (lambda a, b: int(a) * 60 + int(b))(*x.split(':'))
# 	tmd = lambda x: ((lambda a, b: (tm(a), tm(b)))(*x.split('-')))
# 	tmdin = lambda x, y: x[0] >= y[0] and x[1] <= y[1]
# 	width = lambda x: x['DimensionsSummer']['Width']
# 	length = lambda x: x['DimensionsSummer']['Length']
# 	mon = lambda x: x['WorkingHoursSummer']['Понедельник']
#
# 	open_pools = filter(lambda x: tmdin(tmd('10:00-12:00'), tmd(mon(x))), json.load(fi))
# 	max_pool = max(open_pools, key=lambda x:(length(x), width(x)))
#
# 	print(f"{length(max_pool)}x{width(max_pool)}\n{max_pool['Address']}")
