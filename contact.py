contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts[name] = {'Phone': phone, 'Email': email}

def view_contacts():
    for name, info in contacts.items():
        print(f"{name}: Phone - {info['Phone']}, Email - {info['Email']}")

def edit_contact():
    name = input("Enter the name to edit: ")
    if name in contacts:
        phone = input("New phone: ")
        email = input("New email: ")
        contacts[name] = {'Phone': phone, 'Email': email}
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
    else:
        print("Contact not found.")

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Edit Contact\n4. Delete Contact\n5. Exit")
    choice = input("Choose an option: ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        edit_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        break
    else:
        print("Invalid choice.")