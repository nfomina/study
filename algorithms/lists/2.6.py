# Определение двусвязного списка.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class Solution:
    def reorderList(self, head: ListNode, tail: ListNode) -> ListNode:
        newList = DoublyLinkedList()
        while head or tail:
            if head != tail:
                newList.append(head.val)
                newList.append(tail.val)
                current_head = head
                current_tail = tail
                head = head.next
                tail = tail.prev
                if current_head == tail and current_tail == head:
                    break
            else:
                newList.append(head.val)
                break
        return newList.head


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, new_data):
        new_node = ListNode(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last
        self.tail = new_node
        return
    def printList(self, node):
        print("\nTraversal in forward direction")
        while node:
            print(" {}".format(node.val))
            last = node
            node = node.next
        print("\nTraversal in reverse direction")
        while last:
            print(" {}".format(last.val))
            last = last.prev

new_list = DoublyLinkedList()
for item in [11, 0, 17, 5, 4, 32, 1]:
    new_list.append(item)

res = Solution().reorderList(new_list.head, new_list.tail)
new_l = DoublyLinkedList()
new_l.printList(res)


# such beauty
# class Solution:
#     def reorderList(self, head: ListNode, tail: ListNode) -> ListNode:
#         old = head
#         while head != None and head.next != None and head.next.next != None:
#             oldt = tail
#             tail = tail.prev
#             tail.next = None
#             head.next.prev = oldt
#             oldt.next = head.next
#             head.next = oldt
#             oldt.prev = head
#             head = head.next.next
#         return old