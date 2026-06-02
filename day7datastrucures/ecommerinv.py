# Inventory Management System

inventory = {
    101: ("Laptop", 50000, 10),
    102: ("Mouse", 500, 25),
    103: ("Keyboard", 1500, 0)
}


while True:
    print("\n--- Inventory Menu ---")
    print("1. View Inventory")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Calculate Inventory Value")
    print("5. Show Out-of-Stock Products")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        if inventory:
            print("\nCurrent Inventory:")
            for product, (price, stock) in inventory.items():
                print(f"{product} -> Price: {price}, Stock: {stock}")
        else:
            print("Inventory is empty.")

    elif choice == "2":
        product = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))
        inventory[product] = (price, stock)
        print(f"{product} added successfully!")

    elif choice == "3":
        product = input("Enter product name to update: ")
        if product in inventory:
            new_stock = int(input("Enter new stock quantity: "))
            price = inventory[product][0]  # keep old price
            inventory[product] = (price, new_stock)
            print(f"Stock updated for {product}.")
        else:
            print("Product not found in inventory.")

    elif choice == "4":
        total_value = sum(price * stock for price, stock in inventory.values())
        print(f"Total Inventory Value: {total_value}")

    elif choice == "5":
        print("\nOut-of-Stock Products:")
        out_of_stock = [p for p, (price, stock) in inventory.items() if stock == 0]
        if out_of_stock:
            for product in out_of_stock:
                print(product)
        else:
            print("No products are out of stock.")

    elif choice == "6":
        print("Exiting Inventory System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
