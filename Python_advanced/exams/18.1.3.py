count = 0

with open('grades.txt') as file:
    lines = file.readlines()
    for line in lines:
        family, mark1, mark2, mark3 = line.split()
        if int(mark1) >= 65 and int(mark2) >= 65 and int(mark3) >= 65:
            count += 1

print(count)