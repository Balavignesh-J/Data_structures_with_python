class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def create(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
        else:
            cur=self.head
            while cur.next:
                cur=cur.next
            cur.next=new

    def display(self):
        cur=self.head
        while cur:
            print(cur.data)
            cur=cur.next


ll=LinkedList()
print("Linked List Operations")
print("Menu")
print("1.Add \n2.Insert \n3.Delete \n4.Display \n5.Exit")

while True:
    n=int(input("Enter your choice: "))
    if n==1:
        n=int(input("enter the value:"))
        ll.create(n)
    elif n==2:
        pos=int(input("Enter the value after to insert: "))
        value=int(input("Enter the value to insert: "))
        ll.insert(pos,value)
    elif n==4:
        ll.display()
    elif n==5:
        break

