def queue_template(cls,name):
    q=cls()
    print(f"Queue operations with {name}")
    print("Menu")

    while True:
        print("1.Enque \n2.Deque \n3.Peek \n4.Display")
        n = int(input("Enter your choice: "))
        if n == 1:
            n = int(input("enter the value:"))
            q.enque(n)
        elif n == 2:
            q.deque()
        elif n == 3:
            q.peek()
        elif n == 4:
            q.display()
        else:
            break

def dequeue_template(cls,name):
    q=cls()
    print(f"Queue operations with {name}")
    print("Menu")
    
    print("1.Enque_front \n2.Deque_front \n3.Enque_rear \n4.Deque_rear \n5.Display")
    while True:
        n = int(input("Enter your choice: "))
        if n == 1:
            n = int(input("enter the value:"))
            q.enque_front(n)
        elif n == 2:
            q.deque_front()
        elif n == 3:
            n = int(input("enter the value:"))
            q.enque_rear(n)
        elif n == 4:
            q.deque_rear()
        elif n==5:
            q.display()
        else:
            break