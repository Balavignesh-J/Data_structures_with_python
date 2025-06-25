class Treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinarysearchTree:
    def __init__(self):
        self.root=None

    def add(self,data):
        node=Treenode(data)
        if not self.root:
            self.root=node
            return
        self.recursiveadd(node,self.root)

    def recursiveadd(self,new_data,node):
        if not node.left and new_data.data<node.data:
            node.left=new_data
            return
        elif not node.right and new_data.data>=node.data:
            node.right=new_data
            return

        if node.left and new_data.data<node.data:
            self.recursiveadd(new_data,node.left)
        if node.right and new_data.data>=node.data:
            self.recursiveadd(new_data,node.right)


    def display(self,depth=0,node=None):
        if not node:
            node=self.root
        print(" "*depth,node.data)
        if node.left:
            self.display(depth+1,node.left)
        if node.right:
            self.display(depth+1,node.right)
    def traversal_display(self):
        inorder=[]
        preorder=[]
        postorder=[]
        self.inorder(self.root,inorder)
        self.preorder(self.root,preorder)
        self.postorder(self.root,postorder)
        print("Inorder:",inorder)
        print("preorder:",preorder)
        print("postorder:",postorder)

    def inorder(self,node,res):
        if not node:
            return None
        else:
            self.inorder(node.left,res)
            res.append(node.data)
            self.inorder(node.right,res)

    def preorder(self,node,res):
        if not node:
            return None
        else:
            res.append(node.data)
            self.preorder(node.left,res)
            self.preorder(node.right,res)

    def postorder(self,node,res):
        if not node:
            return None
        else:
            self.postorder(node.left,res)
            self.postorder(node.right,res)
            res.append(node.data)

 
     def remove(self, root=self.root, key):
        if not root:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # find the min from right subtree
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)
        return root

    def search(self,data):
        nodefound=self.findnode(data,self.root)
        if nodefound:
            print("True")
        else:
            print("False")
    def findnode(self,data,node):
        if not node or node.data==data:
            return node
        if data<node.data:
            return self.findnode(data,node.left)
        elif data>=node.data:
            return self.findnode(data,node.right)


binarysearchTree = BinarysearchTree()
binarysearchTree.add(5)
binarysearchTree.add(1)
binarysearchTree.add(2)
binarysearchTree.add(3)
binarysearchTree.add(4)
binarysearchTree.display()
print("\n")
binarysearchTree.traversal_display()
binarysearchTree.remove(key=4)
binarysearchTree.display()
print("\n")
binarysearchTree.search(3)