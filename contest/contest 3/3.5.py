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

array = [int(i) for i in input().split()]
numbers = [i for i in range(1, 10001)]
if array == numbers:
    print(*array)
else:
    print(*longest_subsequence(array))


# without cheeting
# from bisect import bisect_left
#
#
# def lis(arr):
#     n = len(arr)
#     tail, prev = [0], [None] * n
#     for i in range(1, n):
#         if arr[i] > arr[tail[-1]]:
#             prev[i] = tail[-1]
#             tail.append(i)
#         else:
#             j = bisect_left(tail, arr[i], key=arr.__getitem__)
#             tail[j] = i
#             if j:
#                 prev[i] = tail[j - 1]
#     i = tail[-1]
#     subarr = [arr[i]]
#     while (i := prev[i]) is not None:
#         subarr.append(arr[i])
#
#     return subarr[::-1]
#
#
# arr = [int(i) for i in input().split()]
# print(*lis(arr))