def print_100(start=1, end=100):
    if start <= end:
        print(start)
        print_100(start+1)

print_100()