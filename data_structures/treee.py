

class Node:
    def __init__(self):
        self.label = None
        self.children = list()

def recursivePrint(node, f = 0):
    if f == 0:
        print(node.label)
    f = 1
    if node.children:
        for child in node.children:
            print(child.label)
            if child.children:
                recursivePrint(child, f)

node6 = Node()
node6.label = 'Imbe'
node5 = Node()
node5.label = 'Lemon'
node5.children = [node6]
node4 = Node()
node4.label = 'Mango'
node3 = Node()
node3.label = 'Nectarine'
node3.children = [node4]

node2 = Node()
node2.label = 'Apple'
node2.children = [node3, node5]

node1 = Node()
node1.label = 'Cherry'
node1.children = [node2]

recursivePrint(node6)


# short and smart
# def recursivePrint(node):
#     # YOUR CODE HERE
#     print(node.label)
#     for i in node.children:
#         recursivePrint(i)