def inversions(sequence):
    res = []
    for i, item in enumerate(sequence):
        if i < len(sequence):
            for el in sequence[i+1:]:
                if item > el:
                    res.append((item, el))
    return len(res)


sequence = [3, 1, 4, 2]

print(inversions(sequence))

sequence = [1, 2, 3, 4, 5]

print(inversions(sequence))

sequence = [4, 3, 2, 1]

print(inversions(sequence))

sequence = [1, 1, 1, 1, 1, 1]

print(inversions(sequence))

# def inversions(seq):
#     res, n = 0, len(seq)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if seq[i] > seq[j]:
#                 res += 1
#     return res
