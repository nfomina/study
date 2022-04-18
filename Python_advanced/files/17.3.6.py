letters = 0
words = 0
lines = 0

with open('file.txt') as file:
    line = file.readline()
    while line != '':
        lines += 1
        line = line.split()
        words += len(line)
        letters += sum([len(i) for i in list(filter(lambda x: x.isalpha(), ' '.join(line)))])
        line = file.readline()

print(f'''Input file contains:
{letters} letters 
{words} words 
{lines} lines ''')


# easy way
# with open('lines.txt') as f:
#     txt = f.read()
#     print('Input file contains:')
#     print(sum(map(str.isalpha, txt)), 'letters')
#     print(len(txt.split()), 'words')
#     print(txt.count('\n') + 1, 'lines')