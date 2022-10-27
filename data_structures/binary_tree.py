

class Node:
    def __init__(self):
        self.label = None
        self.parent = None
        self.leftChild = None
        self.rightChild = None


def sortedPrint(node):
    if node:
        if node.leftChild:
            sortedPrint(node.leftChild)
        print(str(node.label))
        if node.rightChild:
            sortedPrint(node.rightChild)



# Cherry -> Apple
# Cherry -> Lemon
# Lemon -> Imbe
# Lemon -> Nectarine
# Nectarine -> Mango

a = Node()
