# Print a pyramid of stars.
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
    
# Keep asking for a password until the correct one is entered.
password = "secret"
while True:
    entered_password = input("Enter the password: ")
    if entered_password == password:
        print("Correct password entered.")
        break
    
# Print all prime numbers from 1 to 100.
for num in range(2, 102):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)

# Create a simple ATM menu that repeats until Exit is chosen.
while True:
    print("ATM Menu:")
    print("1 for Check Balance")
    print("2 for Deposit")
    print("3.for Withdraw")
    print("4 for Exit")
    action=input("Enter your action: ")
    action=int(action)
    if choice == "1":
        print("Your balance is $1000.")
    elif choice == "2":
        amount = float(input("Enter the amount to deposit: "))
        print(f"${amount} deposited successfully.")
    elif choice == "3":
        amount = float(input("Enter the amount to withdraw: "))
        print(f"${amount} withdrawn successfully.")
    elif choice == "4":
        print("Thank you for using the ATM.")
        break
    else:
        print("Invalid choice. Please try again.")