def nonempty_lines(file):
    with open(file, 'r', encoding='utf-8') as f:
        file_lines = (line for line in f)
        for line in file_lines:
            if len(line) > 25:
                yield '...'
            else:
                if line.strip():
                    yield line.strip()


lines = nonempty_lines('data.csv')

print(next(lines))
print(next(lines))
print(next(lines))
print(next(lines))

# one line
# def nonempty_lines(file):
#     with open(file, encoding='utf-8') as f:
#         return (line.strip() if len(line) < 26 else '...' for line in f.readlines() if line.strip())
