# Mini Project 2: Personal Expense Tracker

expenses = []  # list to store expense records

while True:
    print("\n--- Personal Expense Tracker ---")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        desc = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        category = input("Enter category (food, travel, etc.): ")
        expenses.append({"desc": desc, "amount": amount, "category": category})
        print("Expense added successfully!")

    elif choice == "2":
        if expenses:
            print("\nYour Expenses:")
            for i, exp in enumerate(expenses, start=1):
                print(f"{i}. {exp['desc']} - ₹{exp['amount']} ({exp['category']})")
        else:
            print("No expenses recorded yet.")

    elif choice == "3":
        total = sum(exp["amount"] for exp in expenses)
        print(f"Total Expenses: ₹{total}")

    elif choice == "4":
        print("Exiting Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1-4.")
