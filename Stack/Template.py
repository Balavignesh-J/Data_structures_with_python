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

