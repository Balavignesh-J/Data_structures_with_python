class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]

class Tree:
    def __init__(self):
        self.root=None

    def addnode(self,data,parent=None):
        node=TreeNode(data)
        if not self.root:
            self.root=node
            return
        parentnode = self.findnode(parent,self.root)

        if not parentnode:
            print("Parent not found")
            return
        else:
            parentnode.children.append(node)

    def findnode(self,data,node):
        if node.data==data:
            return node
        for child in node.children:
            nodefound=self.findnode(data,child)
            if nodefound:
                return nodefound
        return None

    def display(self,node=None,depth=0):
        if not node:
            node=self.root
        print(" "*depth,node.data)
        for child in node.children:
            self.display(child,depth+1)



t=Tree()
t.addnode(1)
t.addnode(2,1)
t.addnode(3,1)
t.addnode(4,1)
t.addnode(5,2)
t.addnode(6,2)
t.addnode(7,3)
t.addnode(8,4)
t.display()