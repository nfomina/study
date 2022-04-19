n = int(input())

with open('output.txt', 'w') as output_file:
    for _ in range(n):
        with open(input()) as input_file:
            output_file.write(input_file.read())
            output_file.write('\n')