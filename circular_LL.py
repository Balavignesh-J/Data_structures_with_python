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
        new = Node(data)
        cur = self.head
        if self.head.data == pos:
            new.next = self.head.next
            self.head.next = new
            return
        while True:
            if cur == self.head:
                cur = cur.next
            elif cur.next != self.head:
                if cur.data == pos:
                    new.next = cur.next
                    cur.next = new
                    break
                cur = cur.next
            else:
                break

        if cur.next == self.head and cur.data == pos:
            new.next = cur.next
            cur.next = new


cll = Cll()
cll.create(5)
cll.create(6)
cll.insert(7, 4)
cll.display()
