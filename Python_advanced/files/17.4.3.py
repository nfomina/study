

with open('input.txt') as input_file, open('output.txt', 'w') as output_file:
    for i, line in enumerate(input_file.readlines()):
        output_file.write(f'{i+1}) {line}')