from itertools import groupby

H = [int(i) for i in input().split()]

blocks = 0

def change_H(H, blocks):
    min_h = min(H)
    if min_h > 0:
        for i, item in enumerate(H):
            H[i] = H[i] - min_h
        blocks += 1
    return H, blocks

parts = [list(group) for k, group in groupby(H, lambda x: x == 0) if not k]
while len(parts) > 0:
    new_parts = []
    for part in parts:
        part, blocks = change_H(part, blocks)
        if max(part) > 0:
            part = [list(group) for k, group in groupby(part, lambda x: x == 0) if not k]
            new_parts.extend(part)
    parts = new_parts

print(blocks)
