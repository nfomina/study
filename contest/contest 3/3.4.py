n = int(input())


def gen(n: int, counter_open: int, counter_close: int, ans: str):
    if counter_open + counter_close == 2 * n:
        print(ans)
    if counter_open < n:
        gen(n, counter_open + 1, counter_close, ans + '(')
    if counter_open > counter_close:
        gen(n, counter_open, counter_close + 1, ans + ')')


gen(n//2, 0, 0, '')