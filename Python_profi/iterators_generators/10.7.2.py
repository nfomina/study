def parse_ranges(ranges_string):
    ranges = list(map(int, ranges_string.replace(',', ' ').replace('-', ' ').split(' ')))
    borders = []
    for i in range(0, len(ranges), 2):
        borders.append(range(ranges[i], ranges[i+1]+1))
    for border in borders:
        yield from border


print(*parse_ranges('1-2,4-4,8-10'))
print(*parse_ranges('1-10,2-10'))
print(*parse_ranges('7-32'))

# cry
# def parse_ranges(ranges: str):
#     for r in ranges.split(","):
#         start, end = map(int, r.split("-"))
#         yield from range(start, end+1)
