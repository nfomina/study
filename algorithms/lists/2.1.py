

# Определение односвязного списка.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = ''
        while head is not None:
            res += str(head.val)
            head = head.next
        return int(res, 2)




head = ListNode(input())

print(Solution().getDecimalValue(head))

