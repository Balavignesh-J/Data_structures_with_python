def user_template(cls):
    t = cls()
    print(f"\nTrie Operations")
    print("============================")

    def display_all_words(node, prefix, words):
        if node.IsEnd:
            words.append(prefix)
        for char, child in node.children.items():
            display_all_words(child, prefix + char, words)

    while True:
        print("\nMenu:")
        print("1. Add Word")
        print("2. Search Word")
        print("3. Remove Word")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            word = input("Enter the word to add: ").strip()
            t.add(word)
        elif choice == '2':
            word = input("Enter the word to search: ").strip()
            if t.search(word):
                print(f"'{word}' is found in the Trie.")
            else:
                print(f"'{word}' is NOT found in the Trie.")
        elif choice == '3':
            word = input("Enter the word to remove: ").strip()
            t.remove(word)
        elif choice == '4':
            print("Exiting Trie Operations.")
            break
        else:
            print("Invalid choice. Please try again.")