balance = 1000

def display_balance():
    print("Current Balance:", balance)

def deposit(amount):
    global balance
    balance += amount
    print("Amount Deposited Successfully")

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Withdrawal Successful")
    else:
        print("Insufficient Balance")

while True:
    print("\n--- BANK MENU ---")
    print("1. Display Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        display_balance()

    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        deposit(amount)

    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        withdraw(amount)

    elif choice == 4:
        break

    else:
        print("Invalid Choice")
