import re

with open('output.txt', 'w') as output_file, open('logfile.txt') as input_file:
    for line in input_file.readlines():
        name, start_hour, start_minute, end_hour, end_minute, *other = re.split(', |:|\n', line)
        if int(end_hour)*60 + int(end_minute) - int(start_hour)*60 - int(start_minute) >= 60:
            print(name, file=output_file)