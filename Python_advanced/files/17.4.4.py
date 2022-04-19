
with open('class_scores.txt') as input_file, open('new_scores.txt', 'w') as output_file:
    for i, line in enumerate(input_file.readlines()):
        family, score = line.split()
        output_file.write(f'{family} {int(score) + 5 if int(score) <= 95 else 100}' + '\n')
