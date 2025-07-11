contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    contacts[name] = phone

def view_contacts():
    for item in contacts.items():
        print(f"{item[0]} : {item[1]}")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Deleted")
    else:
        print("Contact not found")

while True:
    print("\n1. Add\n2. View\n3. Delete\n4. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")