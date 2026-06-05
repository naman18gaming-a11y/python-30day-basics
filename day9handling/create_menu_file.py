# Menu-driven program: Add, Show, Exit

items = []   # empty list to store added items

while True:
    print("\n--- Menu ---")
    print("1. Add")
    print("2. Show")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        item = input("Enter item to add: ")
        items.append(item)
        print(f"{item} has been added.")

    elif choice == "2":
        if items:
            print("Items:", items)
        else:
            print("No items to show.")

    elif choice == "3":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
