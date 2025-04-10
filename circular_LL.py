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

    def insert(self, data, pos):

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
        flag = False
        while cur.next != self.head and cur.next.data!=data:
            cur=cur.next


        if cur.next.data==data:
            cur.next=cur.next.next
            flag=True

        if flag:
            print("Deletion sucess")
        else:
            print("Element not present")


cll = Cll()
cll.create(5)
cll.create(6)
cll.insert(7, 6)
cll.delete(5)
cll.display()
