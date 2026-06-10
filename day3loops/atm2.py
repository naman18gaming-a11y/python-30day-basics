balance = 1000  # starting balance

while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is:", balance)
    elif choice == "2":
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print("Deposited:", amount, "New balance:", balance)
    elif choice == "3":
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawn:", amount, "New balance:", balance)
        else:
            print("Insufficient balance!")
    elif choice == "4":
        print("Thank you for using the ATM!")
        break
    else:
        print("Invalid choice. Please try again.")
        exit()
