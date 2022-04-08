def pascal(n):
    for i in range(1, n + 1):
        line = 1
        for j in range(1, i + 1):
            print(line, end=' ')
            line = line * (i - j) // j
        print()

pascal(int(input()))