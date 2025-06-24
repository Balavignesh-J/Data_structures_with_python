class Treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None

    def add(self,data):
        node=Treenode(data)
        if not self.root:
            self.root=node
            return
        self.recursiveadd(node,self.root)

    def recursiveadd(self,data,node):
        if not node.left:
            node.left=data
        elif not node.right:
            node.right=data
        else:
            self.recursiveadd(data,node.left)

    def display(self,depth=0,node=None):
        if not node:
            node=self.root
        print(" "*depth,node.data)
        if node.left:
            self.display(depth+1,node.left)
        if node.right:
            self.display(depth+1,node.right)

    def remove(self,data):
        if not self.root:
            print("Tree is empty")
            return
        if self.root.data==data:
            self.root=None
            return
        self.recursiveremove(data,self.root)

    def recursiveremove(self,data,node):
        if node.left and node.left.data==data:
            node.left=None
            return
        if node.right and node.right.data==data:
            node.right=None
            return
        if node.left:
            self.recursiveremove(data,node.left)
        if node.right:
            self.recursiveremove(data,node.right)
    def search(self,data):
        nodefound=self.findnode(data,self.root)
        if nodefound:
            print("True")
        else:
            print("False")
    def findnode(self,data,node):
        if not node or node.data==data:
            return node
        return self.findnode(data,node.left) or self.findnode(data,node.right)


binaryTree = BinaryTree()
binaryTree.add(5)
binaryTree.add(1)
binaryTree.add(2)
binaryTree.add(3)
binaryTree.add(4)
binaryTree.add(5)
binaryTree.display()
print("\n")
binaryTree.remove(4)
binaryTree.display()
print("\n")
binaryTree.search(3)