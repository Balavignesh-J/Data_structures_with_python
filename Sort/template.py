def sorting_template():
    print("\nSorting Algorithms Menu")
    print("=========================")

    while True:
        print("\nMenu:")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")
        print("4. Merge Sort")
        print("5. Quick Sort")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '6':
            print("Exiting Sorting Menu.")
            break

        raw_input = input("Enter the array elements separated by space: ").strip()
        arr = [int(x) for x in raw_input.split()]

        if choice == '1':
            bubble(arr)
            print("Sorted using Bubble Sort:", arr)
        elif choice == '2':
            selection(arr)
            print("Sorted using Selection Sort:", arr)
        elif choice == '3':
            insertion(arr)
            print("Sorted using Insertion Sort:", arr)
        elif choice == '4':
            merge(arr)
            print("Sorted using Merge Sort:", arr)
        elif choice == '5':
            quick(arr, 0, len(arr)-1)
            print("Sorted using Quick Sort:", arr)
        else:
            print("Invalid choice. Please try again.")
