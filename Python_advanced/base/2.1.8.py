def f(n, k):
    if n == 1:
        return 1
    else:
        return ((f(n-1, k) + k -1) % n) + 1

print(f(int(input()), int(input())))