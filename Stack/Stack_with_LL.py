from Template import stack_template

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Sll:
    def __init__(self):
        self.head=None
        self.top=-1

    def isempty(self):
        if self.top==-1:
            return True
        else:
            return False

    def push(self,data):
        new=Node(data)
        if self.isempty():
            self.head=new
            self.top+=1
        else:
            new.next=self.head
            self.head=new
            self.top+=1

    def pop(self):
        if not self.isempty():
            cur=self.head
            self.head=cur.next
            self.top-=1
            print(f"The Popped element is {cur.data}")
        else:
            print("The Stack is Empty")

    def peek(self):
        if not self.isempty():
            cur=self.head
            print(f"The Peek element is {cur.data}")
        else:
            print("The Stack is Empty")

    def display(self):
        if self.isempty():
            print("Stack is empty")
        else:
            cur=self.head
            while cur:
                print(cur.data)
                cur=cur.next

stack_template(Sll,"Stack with Linked List")