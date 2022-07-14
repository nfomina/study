
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        elements = []
        while head:
            elements.append(head.val)
            head = head.next
        elements.reverse()
        head = ListNode(elements[0])
        for element in elements[1:]:
            ptr = head
            while ptr.next:
                ptr = ptr.next
            ptr.next = ListNode(element)
        return head

def make_list(elements):
   head = ListNode(elements[0])
   for element in elements[1:]:
      ptr = head
      while ptr.next:
         ptr = ptr.next
      ptr.next = ListNode(element)
   return head

head = make_list([11, 0, 17, 5, 4, 32])


res = Solution().reverse(head)
while res is not None and res.val is not None:
    print(res.val)
    res = res.next

# Genious
# class Solution:
#     def reverse(self, head: ListNode) -> ListNode:
#         tail = None
#         while head:
#             head.next, tail, head = tail, head, head.next
#         return tail