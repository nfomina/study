class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class Solution:
    def isPalindrome(self, head: ListNode, tail: ListNode) -> bool:
        while head and tail and head.val == tail.val:
            head = head.next
            tail = tail.prev
        if head is None:
            return True
        else:
            return False



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
for item in [11, 0, 17, 5, 4, 32, 4, 5, 17, 0, 11]:
    new_list.append(item)

res = Solution().isPalindrome(new_list.head, new_list.tail)
print(res)