# Contact Book Application

import os  # Import the os module to handle file operations

# Function to load contacts from a file
def load_contacts(filename):
    contacts = {}  # Initialize an empty dictionary to store contacts
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                name, number = line.strip().split(',')
                contacts[name] = number
    return contacts

# Function to save contacts to a file
def save_contacts(filename, contacts):
    with open(filename, 'w') as file:
        for name, number in contacts.items():
            file.write(f"{name},{number}\n")

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter the contact name: ")
    number = input("Enter the contact number: ")
    contacts[name] = number
    print(f"Contact {name} added successfully!")

# Function to view all contacts
def view_contacts(contacts):
    if contacts:
        print("Contact List:")
        for name, number in contacts.items():
            print(f"Name: {name}, Number: {number}")
    else:
        print("No contacts found.")

# Function to delete a contact
def delete_contact(contacts):
    name = input("Enter the contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"Contact {name} not found.")

# Main function to run the contact book application
def main():
    filename = "contacts.txt"  # Define the filename for storing contacts
    contacts = load_contacts(filename)  # Load contacts from the file

    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            save_contacts(filename, contacts)
            print("Contacts saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()