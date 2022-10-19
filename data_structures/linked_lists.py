class Node:
    def __init__(self):
        self.value = None
        self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def __repr__(self):
#         node = self.head
#         nodes = []
#         while node is not None:
#             nodes.append(node.data)
#             node = node.next
#         nodes.append("None")
#         return " -> ".join(nodes)

def find(node, element):
    while node:
        if node.value == element:
            return 'true'
        node = node.next
    return 'false'

def insert(head, newnode, index):
    newNode = Node()
    newNode.value = newnode.value
    if (index == 1):
        newNode.next = head
        head = newNode
    else:
        temp = head
        for i in range(0, index - 1):
            if (temp != None):
                temp = temp.next
        if (temp != None):
            newNode.next = temp.next
            temp.next = newNode

def remove(head, index):
    if head.value == index:
        head = head.next
        return
    current = head
    while current:
        if current.value == index:
            break
        previous = current
        current = current.next
    if current is None:
        print('Deletion Error: Key not found.')
    else:
        previous.next = current.next


#Sample Input:
# 2
# 0 -> 1 -> 2 -> 3 -> 4 -> 5
# Sample Output:
# true
a = Node()
a.value = 5
insert(a, 2, 0)
#
# print(find(a, 2))
