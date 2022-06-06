from bisect import bisect_left

def longest_subsequence(seq):
  bisect = bisect_left
  rank = seq
  rank = list(rank)
  if not rank: return []
  lastoflength = [0]
  predecessor = [None]

  for i in range(1, len(seq)):
    j = bisect([rank[k] for k in lastoflength], rank[i])
    try:
        lastoflength[j] = i
    except:
        lastoflength.append(i)
    predecessor.append(lastoflength[j-1] if j > 0 else None)

  def trace(i):
    if i is not None:
      yield from trace(predecessor[i])
      yield i
  indices = trace(lastoflength[-1])

  return [seq[i] for i in indices]

print(*longest_subsequence([int(i) for i in input().split()]))