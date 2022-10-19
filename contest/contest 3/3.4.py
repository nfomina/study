def gen(n, count, stack, ans):
    if count == n // 2 and len(stack) == 0:
        print(ans)
        return
    if count < n // 2:
        gen(n, count + 1, stack + '(', ans + '(')
        gen(n, count + 1, stack + '[', ans + '[')
    if len(stack) > 0:
        if stack[-1] == '(':
            gen(n, count, stack[:-1], ans + ')')
        if stack[-1] == '[':
            gen(n, count, stack[:-1], ans + ']')


N = int(input())
gen(N, 0, "", "")


# smart
# from collections import deque
#
#
# def brackets(n, count_op=0, ans='', st=deque()):
#     if len(ans) == 2 * n:
#         print(ans)
#         return
#     if count_op < n:
#         for bracket in ('()', '[]'):
#             st.append(bracket[1])
#             brackets(n, count_op + 1,  ans + bracket[0], st.copy())
#             st.pop()
#     if st:
#         brackets(n, count_op, ans + st.pop(), st.copy())
#
#
# brackets(int(input())//2)