from Template import queue_template

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Qll:
    def __init__(self):
        self.front=None
        self.rear=None

    def isempty(self):
        if not self.front:
            return True
        else:
            return False

    def enque(self,data):
        new=Node(data)
        if self.isempty():
            self.front=new
            self.rear=new
        else:
            cur=self.front
            while cur.next:
                cur=cur.next
            cur.next=new
            self.rear=new
           
    def deque(self):
        if not self.isempty():
            cur=self.front
            self.front=cur.next
            print(f"The Dequeued element is {cur.data}")
        else:
            print("The Queue is Empty")

    def peek(self):
        if not self.isempty():
            cur=self.front
            print(f"The Peek element is {cur.data}")
        else:
            print("The Stack is Empty")

    def display(self):
        if self.isempty():
            print("Queue is empty")
        else:
            cur=self.front
            while cur:
                print(cur.data)
                cur=cur.next

queue_template(Qll,"LinkedList")