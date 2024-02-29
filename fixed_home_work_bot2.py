def parse_input(user_input):
    parts = user_input.strip().split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args

def add_contact(contacts, name, phone):
    contacts[name] = phone
    return "Contact added."

def change_contact(contacts, name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_all(contacts):
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")

def show_phone(contacts, name):
    if name in contacts:
        print(f"Phone number for {name}: {contacts[name]}")
    else:
        print("Contact not found.")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) != 2:
                print("Invalid command format. Use: add [name] [phone]")
            else:
                name, phone = args
                print(add_contact(contacts, name, phone))
        elif command == "change":
            if len(args) != 2:
                print("Invalid command format. Use: change [name] [new_phone]")
            else:
                name, new_phone = args
                print(change_contact(contacts, name, new_phone))
        elif command == "all":
            show_all(contacts)
        elif command == "phone":
            if len(args) != 1:
                print("Invalid command format. Use: phone [name]")
            else:
                name = args[0]
                show_phone(contacts, name)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
