def template(cls,name):
    ll = cls()
    print(f"{name} Operations")
    print("Menu")

    while True:
        print("1.Add \n2.Insert \n3.Delete \n4.Display")
        n = int(input("Enter your choice: "))
        if n == 1:
            n = int(input("enter the value:"))
            ll.create(n)
        elif n == 2:
            pos = int(input("Enter the value after to insert: "))
            value = int(input("Enter the value to insert: "))
            ll.insert(pos, value)
        elif n == 3:
            value = int(input("Enter the node to delete: "))
            ll.delete(value)
        elif n == 4:
            ll.display()
        else:
            break

def stack_template(cls,name):
    s=cls()
    print(f"Stack operations with {name}")
    print("Menu")

    while True:
        print("1.Push \n2.Pop \n3.Peek \n4.Display")
        n = int(input("Enter your choice: "))
        if n == 1:
            n = int(input("enter the value:"))
            s.push(n)
        elif n == 2:
            s.pop()
        elif n == 3:
            s.peek()
        elif n == 4:
            s.display()
        else:
            break


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
