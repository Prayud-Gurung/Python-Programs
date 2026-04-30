#dictionary {name: [email, contact]}

contactList:dict = {}

def add_contact():
    name = input("Enter name: ")
    email = input("Enter email: ")
    contact = input("Enter contact number: ")

    contactList[name] = [email, contact]

def show_contacts():
    print("\nContacts\n")
    for name in contactList:
        print("* " + name)

def search_contact():
    search = input("Find: ")
    found = False

    for name, details in contactList.items():
        if search in name.lower():
            email, contact = details
            print("\nContact found:")
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Contact: {contact}")
            found = True

    if not found:
        print("No matching contact found.\n")

def remove_contact():
    contact = input("Delete: ")
    if contact in contactList.keys():
        contactList.pop(contact)
        print("Contact removed")
    else:
        print("Could not find contact: ")

def update_contact():
    contact = input("Enter contact to update")
    if contact in contactList.keys():
        email = input("Enter new email: ")
        number = input("Enter new contact number: ")
        contactList[contact] = [email, number]
while True:
    print("\nWelcome")
    print("Enter 1 to add Contact")
    print("Enter 2 to show contact")
    print("Enter 3 to search contact")
    print("Enter 4 to remove contact")
    print("Enter 5 to update contact")
    print("Enter 6 to end")

    operation = input("What operation you want to do? : ")

    match operation:
        case "1":
            add_contact()
        case "2":
            show_contacts()
        case "3":
            search_contact()
        case "4":
            remove_contact()
        case "5":
            update_contact()
        case "6":
            break
        case _:
            print("invalid choice")