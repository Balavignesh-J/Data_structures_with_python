from Template import queue_template

class Q:
    def __init__(self):
        self.queue=[]
        self.front=0
        self.rear=0
        self.size=10
        self.count=0

    def isempty(self):
        if self.front==self.rear:
            return True
        else:
            return False
    
    def qfull(self):
        return self.count==self.size
            

    def enque(self,n):
        if not self.qfull():       
            self.queue.append(n)
            self.rear+=1
            self.count+=1
            print("Enque success")

    def deque(self):
        if not self.isempty():
            n=self.queue.pop(0)
            self.front+=1
            print(f"The deleted element is {n}")
        else:
            print("Queue is empty")

    def next_del(self):
        if not self.isempty():
            n=self.queue[0]
            print(f"The Top element is {n}")
        else:
            print("Queue is empty")

    def display(self):
        if not self.isempty():
            for i in range(self.front,self.rear):
                print(f"{i+1} element is {self.queue[i]}")
        else:
            print("Queue is empty")


queue_template(Q,"Array")