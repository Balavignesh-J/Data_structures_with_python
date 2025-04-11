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

    def insert(self,pos,value):
        if self.head is not None:
            new=Node(value)
            cur=self.head
            while cur:
                if cur.data==pos or cur.next is None:
                    new.next=cur.next
                    cur.next=new
                    print("Insert sucess")
                    break
                else:
                    cur=cur.next
        else:
            print("Linked List is empty")

    def delete(self, value):
        if self.head is not None:
            if self.head.data==value and self.head.next is None:
                self.head=None
            elif self.head.data==value and self.head.next is not None:
                self.head=self.head.next
            else:
                cur=self.head
                while cur:
                    if cur.next.data==value:
                        cur.next=cur.next.next
                        print("Deletion sucess")
                        break
                    else:
                        cur=cur.next
        else:
            print("Linked List is empty")

    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            cur=self.head
            while cur:
                print(cur.data)
                cur=cur.next


ll=LinkedList()
print("Linked List Operations")
print("Menu")

while True:
    print("1.Add \n2.Insert \n3.Delete \n4.Display")
    n=int(input("Enter your choice: "))
    if n==1:
        n=int(input("enter the value:"))
        ll.create(n)
    elif n==2:
        pos=int(input("Enter the value after to insert: "))
        value=int(input("Enter the value to insert: "))
        ll.insert(pos,value)
    elif n==3:
        value=int(input("Enter the node to delete: "))
        ll.delete(value)
    elif n==4:
        ll.display()
    else:
        break

