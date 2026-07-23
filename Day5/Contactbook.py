# Simple Contact Book 
contact_book={}
while True:
    print('''Choose your action:
          (1) Add Contact
          (2) View Contacts
          (3) Search Contact
          (4) Delete Contact
          (5) Exit''')
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contact_book[name] = phone
        print("Contact added successfully!")
    elif choice == "2":
        if contact_book:
            print("Contacts:")
            for name, phone in contact_book.items():
                print(f"{name}: {phone}")
        else:
            print("No contact_book found.")
    elif choice == "3":
        name = input("Enter name to search: ")
        if name in contact_book:
            print(f"{name}'s phone number is {contact_book[name]}")
        else:
            print("Contact not found.")
    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in contact_book:
            del contact_book[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")