def template(cls):
    ll = cls()
    print("Double Linked List Operations")
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