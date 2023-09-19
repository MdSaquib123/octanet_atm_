# Initialize the user database as a dictionary
user_database = {}


# Function to register a new user
def register_user():
    username = input("Enter your username: ")
    if username in user_database:
        print("Username already exists. Please choose a different username.")
    else:
        password = input("Enter your password: ")
        balance = float(input("Enter your initial balance: "))
        user_database[username] = {"password": password, "balance": balance, "history": []}
        print("Registration successful!")


# Function to check account balance
def check_balance(username):
    if username in user_database:
        password = input("Enter your password: ")
        if password == user_database[username]["password"]:
            balance = user_database[username]["balance"]
            print(f"Your account balance is: ${balance:.2f}")
        else:
            print("Incorrect password.")
    else:
        print("Invalid username. Please register first.")


# Function to withdraw money
def withdraw(username):
    if username in user_database:
        password = input("Enter your password: ")
        if password == user_database[username]["password"]:
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= 0:
                print("Please enter a valid withdrawal amount.")
            elif amount <= user_database[username]["balance"]:
                user_database[username]["balance"] -= amount
                user_database[username]["history"].append(f"Withdrawal of ${amount:.2f}")
                print(f"Withdrawal successful. Remaining balance: ${user_database[username]['balance']:.2f}")
            else:
                print("Insufficient balance.")
        else:
            print("Incorrect password.")
    else:
        print("Invalid username. Please register first.")


# Function to deposit money
def deposit(username):
    if username in user_database:
        password = input("Enter your password: ")
        if password == user_database[username]["password"]:
            amount = float(input("Enter the amount to deposit: "))
            if amount <= 0:
                print("Please enter a valid deposit amount.")
            else:
                user_database[username]["balance"] += amount
                user_database[username]["history"].append(f"Deposit of ${amount:.2f}")
                print(f"Deposit successful. New balance: ${user_database[username]['balance']:.2f}")
        else:
            print("Incorrect password.")
    else:
        print("Invalid username. Please register first.")


# Function to transfer money
def transfer(username):
    if username in user_database:
        password = input("Enter your password: ")
        if password == user_database[username]["password"]:
            recipient = input("Enter recipient's username: ")
            if recipient in user_database:
                amount = float(input("Enter the amount to transfer: "))
                if amount <= 0:
                    print("Please enter a valid transfer amount.")
                elif amount <= user_database[username]["balance"]:
                    user_database[username]["balance"] -= amount
                    user_database[recipient]["balance"] += amount
                    user_database[username]["history"].append(f"Transfer of ${amount:.2f} to {recipient}")
                    user_database[recipient]["history"].append(f"Received ${amount:.2f} from {username}")
                    print("Transfer successful.")
                else:
                    print("Insufficient balance.")
            else:
                print("Recipient's username not found.")
        else:
            print("Incorrect password.")
    else:
        print("Invalid username. Please register first.")


# Function to view transaction history
def view_transaction_history(username):
    if username in user_database:
        print("Transaction History:")
        for transaction in user_database[username]["history"]:
            print(transaction)
    else:
        print("Invalid username. Please register first.")


# Main program loop
while True:
    print("\nATM Menu:")
    print("0. Register")
    print("1. Balance Inquiry")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Transfer")
    print("5. View Transaction History")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == "0":
        register_user()
    elif choice == "1":
        username = input("Enter your username: ")
        check_balance(username)
    elif choice == "2":
        username = input("Enter your username: ")
        withdraw(username)
    elif choice == "3":
        username = input("Enter your username: ")
        deposit(username)
    elif choice == "4":
        username = input("Enter your username: ")
        transfer(username)
    elif choice == "5":
        username = input("Enter your username: ")
        view_transaction_history(username)
    elif choice == "6":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")