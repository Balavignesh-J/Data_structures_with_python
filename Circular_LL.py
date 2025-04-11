class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Cll:
    def __init__(self):
        self.head = None

    def create(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
            new.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new
            new.next = self.head

    def display(self):
        cur = self.head
        while True:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def insert(self, pos ,data):

        if self.head==None:
            print("List is empty")
            return

        new=Node(data)
        cur=self.head
        flag=False
        while cur.next!=self.head:
            if cur.data==pos:
                new.next=cur.next
                cur.next=new
                flag=True
                break
            else:
                cur=cur.next

        if not flag and cur.data==pos:
            new.next = cur.next
            cur.next = new

    def delete(self,data):
        cur = self.head
        if self.head.data==data:
            while cur.next!=self.head:
                cur=cur.next
            cur.next=self.head.next
            self.head=self.head.next
            print("Deletion success")
            return
        flag = False
        while cur.next != self.head and cur.next.data!=data:
            cur=cur.next


        if cur.next.data==data:
            cur.next=cur.next.next
            flag=True

        if flag:
            print("Deletion success")
        else:
            print("Element not present")


cll = Cll()

print("Circular Linked List Operations")
print("Menu")

while True:
    print("1.Add \n2.Insert \n3.Delete \n4.Display")
    n=int(input("Enter your choice: "))
    if n==1:
        n=int(input("enter the value:"))
        cll.create(n)
    elif n==2:
        pos=int(input("Enter the value after to insert: "))
        value=int(input("Enter the value to insert: "))
        cll.insert(pos,value)
    elif n==3:
        value=int(input("Enter the node to delete: "))
        cll.delete(value)
    elif n==4:
        cll.display()
    else:
        break
