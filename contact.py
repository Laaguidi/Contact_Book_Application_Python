# Contact Book Application

import os  # Import the os module to handle file operations

# Function to load contacts from a file
def load_contacts(filename):
    contacts = {}  # Initialize an empty dictionary to store contacts
    if os.path.exists(filename):  # Check if the file exists
        with open(filename, 'r') as file:  # Open the file in read mode
            for line in file:  # Iterate over each line in the file
                name, number = line.strip().split(',')  # Split the line into name and number
                contacts[name] = number  # Add the contact to the dictionary
    return contacts  # Return the dictionary of contacts

# Function to save contacts to a file
def save_contacts(filename, contacts):
    with open(filename, 'w') as file:  # Open the file in write mode
        for name, number in contacts.items():  # Iterate over each contact
            file.write(f"{name},{number}\n")  # Write the contact to the file

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter the contact name: ")  # Prompt the user for the contact name
    number = input("Enter the contact number: ")  # Prompt the user for the contact number
    contacts[name] = number  # Add the new contact to the dictionary
    print(f"Contact {name} added successfully!")  # Inform the user that the contact was added

# Function to view all contacts
def view_contacts(contacts):
    if contacts:  # Check if there are any contacts
        print("Contact List:")  # Print the heading for the contact list
        for name, number in contacts.items():  # Iterate over each contact
            print(f"Name: {name}, Number: {number}")  # Print the contact details
    else:
        print("No contacts found.")  # Inform the user if there are no contacts

# Function to delete a contact
def delete_contact(contacts):
    name = input("Enter the contact name to delete: ")  # Prompt the user for the contact name to delete
    if name in contacts:  # Check if the contact exists in the dictionary
        del contacts[name]  # Delete the contact from the dictionary
        print(f"Contact {name} deleted successfully!")  # Inform the user that the contact was deleted
    else:
        print(f"Contact {name} not found.")  # Inform the user if the contact was not found

# Main function to run the contact book application
def main():
    filename = "contacts.txt"  # Define the filename for storing contacts
    contacts = load_contacts(filename)  # Load contacts from the file

    while True:  # Start an infinite loop for the menu
        print("\nContact Book Menu")  # Print the menu heading
        print("1. Add Contact")  # Print the option to add a contact
        print("2. View Contacts")  # Print the option to view contacts
        print("3. Delete Contact")  # Print the option to delete a contact
        print("4. Exit")  # Print the option to exit the application
        choice = input("Enter your choice: ")  # Prompt the user to enter their choice

        if choice == '1':  # If the user chooses to add a contact
            add_contact(contacts)  # Call the function to add a contact
        elif choice == '2':  # If the user chooses to view contacts
            view_contacts(contacts)  # Call the function to view contacts
        elif choice == '3':  # If the user chooses to delete a contact
            delete_contact(contacts)  # Call the function to delete a contact
        elif choice == '4':  # If the user chooses to exit
            save_contacts(filename, contacts)  # Save the contacts to the file
            print("Contacts saved. Exiting the program.")  # Inform the user that contacts are saved and the program is exiting
            break  # Break the loop to exit the program
        else:
            print("Invalid choice. Please try again.")  # Inform the user if they entered an invalid choice

if __name__ == "__main__":  # Check if the script is being run directly (not imported as a module)
    main()  # Call the main function to start the program