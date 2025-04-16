import collections
from Template import dequeue_template

class Q:
    def __init__(self):
        self.queue = collections.deque()
        self.size = 10
        self.count = 0
    
    def isempty(self):
        return len(self.queue) == 0
        
    def qfull(self):
        return self.count == self.size

    def enque_front(self, n):
        if not self.qfull():
            self.queue.appendleft(n)
            self.count += 1
            print("Enqueue at front success")
        else:
            print("Queue is full")

    def enque_rear(self, n):
        if not self.qfull():
            self.queue.append(n)
            self.count += 1
            print("Enqueue at rear success")
        else:
            print("Queue is full")

    def deque_front(self):
        if not self.isempty():
            n = self.queue.popleft()
            self.count -= 1
            print(f"The deleted element from front is {n}")
        else:
            print("Queue is empty")
    
    def deque_rear(self):
        if not self.isempty():
            n = self.queue.pop()
            self.count -= 1
            print(f"The deleted element from rear is {n}")
        else:
            print("Queue is empty")

    def display(self):
        if not self.isempty():
            for i, val in enumerate(self.queue):
                print(f"{i+1} element is {val}")
        else:
            print("Queue is empty")


dequeue_template(Q, "Array")