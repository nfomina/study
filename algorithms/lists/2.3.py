class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertIntoSorted(self, head: ListNode, new_value: int) -> ListNode:
        p = head
        flag = 0
        while p and p.next:
            if p.val >= new_value or (p.val < new_value and flag == 1):
                p = p.next
            else:
                if head.val <= new_value:
                    node = ListNode(new_value)
                    node.next = head
                    head = node
                else:
                    p_ = None
                    n = head
                    while n != p:
                        p_ = n
                        n = n.next
                    m = ListNode(new_value)
                    m.next = p_.next
                    p_.next = m
                flag = 1
        if flag==0:
            if p.val >= new_value:
                p.next = ListNode(new_value)
            else:
                p_ = None
                n = head
                while n != p:
                    p_ = n
                    n = n.next
                m = ListNode(new_value)
                m.next = p_.next
                p_.next = m
        return head



def make_list(elements):
   head = ListNode(elements[0])
   for element in elements[1:]:
      ptr = head
      while ptr.next:
         ptr = ptr.next
      ptr.next = ListNode(element)
   return head

head = make_list([11, 0])


res = Solution().insertIntoSorted(head, -2)
while res is not None and res.val is not None:
    print(res.val)
    res = res.next