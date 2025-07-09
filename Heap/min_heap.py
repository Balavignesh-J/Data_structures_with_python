class Node:
    def __init__(self,data):
        self.node=data
        self.left=None
        self.right=None

class min_heap:
    def __init__(self):
        self.root=None

    def add(self,n):
        if not self.root:
            self.root=Node(n)
            return
        self.recursiveadd(n,self.root)

    def recursiveadd(self,n,node):
        if not node.left:
            node.left=Node(n)
            self.heapify_up(node.left)
        elif not node.right:
            node.right=Node(n)
            self.heapify_up(node.right)
        else:
            if self.get_count(node.left) > self.get_count(node.right):
                self.recursiveadd(n,node.right)
            else:
                self.recursiveadd(n,node.left)

    def get_count(self,node):
        if not node:
            return 0

        return 1 + self.get_count(node.left) + self.get_count(node.right)

    def heapify_up(self,node):
        while node and node!=self.root:
            parent=self.get_parent(node,self.root)
            if parent.data > node.data:
                parent.data,node.data=node.data,parent.data
                node=parent
            else:
                break

    def get_parent(self,node,root):
        if root.left == node and root.right == node:
            return root

        if root.left:
            parent=self.get_parent(node,root.left)
            if parent:
                return parent
        if root.right:
            parent=self.get_parent(node,root.right)
            if parent:
                return parent

        return None
