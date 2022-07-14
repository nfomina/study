# Определение односвязного списка.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def make_list(self, elements):
        head = ListNode(elements[0])
        for element in elements[1:]:
            ptr = head
            while ptr.next:
                ptr = ptr.next
            ptr.next = ListNode(element)
        return head
    def deleteNode(self, node, data):
        while node.val is not data:
            node = node.next
        try:
            node.val = node.next.val
            node.next = node.next.next
        except:
            node.val = None
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        self.head = head
        uniq_set = set()
        while head is not None:
            if head.val in uniq_set:
                self.deleteNode(head, head.val)
            else:
                uniq_set.add(head.val)
                head = head.next
        current_node = self.head
        res = []
        while current_node is not None and current_node.val is not None:
            res.append(str(current_node.val))
            current_node = current_node.next
        result = self.make_list(res)
        return result




def make_list(elements):
   head = ListNode(elements[0])
   for element in elements[1:]:
      ptr = head
      while ptr.next:
         ptr = ptr.next
      ptr.next = ListNode(element)
   return head

def list_to_str(l):
    a = '->'.join(l)
    return a

head = make_list([1,4,6,7,9,9,10,11,14,14])

Solution().deleteDuplicates(head)
print((Solution().deleteDuplicates(head)))


# easy way
# class Solution:
#     def deleteDuplicates(self, head: ListNode) -> ListNode:
#         p = head
#         while p and p.next:
#             if p.val == p.next.val:
#                 p.next = p.next.next
#             else:
#                 p = p.next
#         return head