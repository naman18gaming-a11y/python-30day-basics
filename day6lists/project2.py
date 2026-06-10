# Shopping Cart Program

cart = []   # start with an empty cart

while True:
    print("\n--- Shopping Cart Menu ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Count Items")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        item = input("Enter item to add: ")
        cart.append(item)
        print(f"{item} has been added to the cart.")

    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
            print(f"{item} has been removed from the cart.")
        else:
            print("Item not found in the cart.")

    elif choice == "3":
        print("Items in the cart:", cart)

    elif choice == "4":
        print("Total items in the cart:", len(cart))

    elif choice == "5":
        print("Exiting shopping cart. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
