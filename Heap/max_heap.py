from template import min_heap_template

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Max_Heap:
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
            if parent.data < node.data:
                parent.data,node.data=node.data,parent.data
                node=parent
            else:
                break

    def get_parent(self,node,root):
        if root.left == node or root.right == node:
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

    def extract_max(self):
        if not self.root:
            print("Root is empty")
            return
        min=self.root.data
        last_node=self.get_lastNode(self.root)
        if last_node:
            self.root.data=last_node.data
            self.heapify_down(self.root)
        else:
            self.root=None
        return min

    def get_lastNode(self,node):
        q=[node]
        last=node
        while q:
            n=q.pop(0)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

            if not n.left and not n.right:
                last=n

        if last!=node:
            parent = self.get_parent(last, self.root)
            if parent.left == last:
                parent.left = None
            if parent.right == last:
                parent.right = None

        return last

    def heapify_down(self,node):
        while node:
            large=node
            if node.left and node.left.data>large.data:
                large=node.left
            if node.right and node.right.data>large.data:
                large=node.right

            if large!=node:
                large.data,node.data=node.data,large.data
                large=node
            else:
                break

    def display(self):
        if not self.root:
            print("Heap is empty")
            return
        q=[self.root]
        while q:
            n=q.pop(0)
            print(n.data,end=' ')
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        print()

min_heap_template(Max_Heap,'Max')