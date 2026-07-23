# Simple Banking System
balance = 0
def deposit():
    global balance
    amount = float(input("Enter deposit amount: "))
    if amount > 0:
        balance += amount
        print(f"{amount} deposited successfully.")
    else:
        print("Invalid amount!")
def withdraw():
    global balance
    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        print("Invalid amount!")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print(f"{amount} withdrawn successfully.")
def check_balance():
    print(f"Current Balance:{balance}")

name = input("Enter your name: ")
while True:
    print('''BANKING SYSTEM
    1. Deposit
    2. Withdraw
    3. Check Balance
    4. Exit''')
    choice = input("Enter your choice: ")
    if choice == "1":
        deposit()
    elif choice == "2":
        withdraw()
    elif choice == "3":
        check_balance()
    elif choice == "4":
        print(f"Thank you, {name}, for using the Banking System!")
        break
    else:
        print("Invalid choice! Please try again.")