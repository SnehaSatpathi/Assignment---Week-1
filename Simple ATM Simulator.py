# Simple ATM Simulator : User login (PIN-based), Options: check balance, deposit, withdraw, Use functions for each operation

def login(pin):
    return pin == "1234"

def check_balance(balance):
    print("Balance:", balance)

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient funds")
        return balance
    return balance - amount

balance = 1000
pin = input("Enter PIN: ")

if login(pin):
    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Choose option: ")
        
        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            amt = float(input("Enter deposit amount: "))
            balance = deposit(balance, amt)
        elif choice == "3":
            amt = float(input("Enter withdraw amount: "))
            balance = withdraw(balance, amt)
        elif choice == "4":
            print("Thank you for using ATM")
            break
        else:
            print("Invalid option")
else:
    print("Wrong PIN")

