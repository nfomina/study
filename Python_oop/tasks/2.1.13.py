def annual_return(start, percent, years):
    for i in range(years):
        start = start*(100+percent)/100
        yield start



for value in annual_return(120000, 10, 3):
    print(round(value))

for value in annual_return(70000, 8, 10):
    print(round(value))
