def min_heap_template(cls,name):
    h = cls()
    print(f"\n{name} Heap Operations")
    print("====================")

    while True:
        print("\nMenu:")
        print("1. Add Element")
        print("2. Display Heap (level-order)")
        print(f"3. Extract {name}")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            val = int(input("Enter value to insert: ").strip())
            h.add(val)
            print(f"Inserted {val} into the heap.")
        elif choice == '2':
            print("Current Heap:")
            h.display()
        elif choice == '3':
            val = h.extract_max()
            if val is not None:
                print(f"Extracted {name} Value: {val}")
        elif choice == '4':
            print(f"Exiting {name} Heap Operations.")
            break
        else:
            print("Invalid choice. Please enter 1 to 4.")
