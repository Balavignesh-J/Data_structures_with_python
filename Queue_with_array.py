class Q:
    def __init__(self):
        self.queue=[]
        self.size=10

    def isempty(self):
        if len(self.queue)==0:
            return True
        else:
            return False
    
    def qfull(self):
        return self.size==len(self.queue)
            

    def enque(self,n):
        if not self.qfull():       
            self.queue.append(n)
            print("Enque success")

    def deque(self):
        if not self.isempty():
            n=self.queue.pop(0)
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
            for i,val in enumerate(self.queue):
                print(f"{i+1} element is {val}")
        else:
            print("Queue is empty")

def queue_template(cls,name):
    q=cls()
    print(f"Queue operations with {name}")
    print("Menu")

    while True:
        print("1.Enque \n2.Deque \n3.Next delete \n4.Display")
        n = int(input("Enter your choice: "))
        if n == 1:
            n = int(input("enter the value:"))
            q.enque(n)
        elif n == 2:
            q.deque()
        elif n == 3:
            q.next_del()
        elif n == 4:
            q.display()
        else:
            break

queue_template(Q,"Array")