"""

@Author: TarunSai
@Date: 2024-09-03
@Last Modified by: Tarunsai
@Last Modified time: 
@Title : Addressbook.

"""

class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, ph_no, email):
        self.firstname = first_name
        self.lastname = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.mobile = ph_no
        self.email = email
    
    def __str__(self):
        return (f"Name: {self.firstname} {self.lastname}, Address: {self.address}, City: {self.city}, "
                f"State: {self.state}, Zip: {self.zip_code}, Phone: {self.mobile}, Email: {self.email}")

class AddressBook:
    def __init__(self, name):
        self.name = name
        self.contacts = {}
    
    def add_contact(self, contact):
        key = (contact.firstname.lower(), contact.lastname.lower())
        
        if key not in self.contacts:
            self.contacts[key] = {}
        
        if contact.email in self.contacts[key]:
            print("Contact already exists.")
        else:
            self.contacts[key][contact.email] = contact
            print("Contact added successfully.")
        
    @staticmethod
    def get_input(prompt):
        return input(prompt)
    
    def update_person(self):
        name = self.get_input("Enter person name to update (format: first_name last_name): ")
        name_parts = name.split()
        if len(name_parts) != 2:
            print("Invalid format. Please enter in 'first_name last_name' format.")
            return

        first_name, last_name = name_parts
        key = (first_name.lower(), last_name.lower())
        
        if key in self.contacts:
            print("Current details:")
            for contact in self.contacts[key].values():
                print(contact)
            
            email = self.get_input("Enter email of the person to update: ")
            if email in self.contacts[key]:
                person = self.contacts[key][email]
                
                new_city = self.get_input("Enter new city (leave blank to keep current): ")
                new_state = self.get_input("Enter new state (leave blank to keep current): ")
                new_zip = self.get_input("Enter new zip code (leave blank to keep current): ")
                new_mobile = self.get_input("Enter new phone number (leave blank to keep current): ")
                
                # Update only if new values are provided
                if new_city:
                    person.city = new_city
                if new_state:
                    person.state = new_state
                if new_zip:
                    try:
                        person.zip_code = int(new_zip)
                    except ValueError:
                        print("Invalid zip code. Keeping the current value.")
                if new_mobile:
                    try:
                        person.mobile = new_mobile
                    except ValueError:
                        print("Invalid phone number. Keeping the current value.")
                
                print("Updated details:")
                print(person)
            else:
                print(f"No contact found with the email {email}.")
        else:
            print(f"No person found with the name {name}.")

    def delete_contact(self):
        name = self.get_input("Enter person name to delete (format: first_name last_name): ")
        name_parts = name.split()
        if len(name_parts) != 2:
            print("Invalid format. Please enter in 'first_name last_name' format.")
            return

        first_name, last_name = name_parts
        key = (first_name.lower(), last_name.lower())

        if key in self.contacts:
            email = self.get_input("Enter email of the person to delete: ")
            if email in self.contacts[key]:
                del self.contacts[key][email]
                if not self.contacts[key]:  # Remove the key if no contacts are left
                    del self.contacts[key]
                print(f"Contact with email {email} deleted.")
            else:
                print(f"No contact found with the email {email}.")
        else:
            print(f"No person found with the name {name}.")

    def add_multiple_contacts(self):
        while True:
            print("\nEnter details for a new contact:")
            first_name = self.get_input("First name: ")
            last_name = self.get_input("Last name: ")
            address = self.get_input("Address: ")
            city = self.get_input("City: ")
            state = self.get_input("State: ")
            zip_code = self.get_input("Zip code: ")
            phone_number = self.get_input("Phone number: ")
            email = self.get_input("Email: ")
            
            if not first_name or not last_name or not email:
                print("First name, last name, and email are required.")
                continue

            try:
                zip_code = int(zip_code)
                phone_number = int(phone_number)
            except ValueError:
                print("Invalid zip code or phone number. They must be integers.")
                continue
            
            contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
            self.add_contact(contact)
            
            another = self.get_input("Do you want to add another contact? (yes/no): ").strip().lower()
            if another != 'yes':
                break
    
    def display_menu(self):
        print("\nAddress Book Menu:")
        print("1. Add a contact")
        print("2. Update a contact")
        print("3. Delete a contact")
        print("4. Add multiple contacts")
        print("5. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = self.get_input("Enter your choice: ").strip()

            if choice == '1':
                print("\nAdd a contact")
                first_name = self.get_input("First name: ")
                last_name = self.get_input("Last name: ")
                address = self.get_input("Address: ")
                city = self.get_input("City: ")
                state = self.get_input("State: ")
                zip_code = self.get_input("Zip code: ")
                phone_number = self.get_input("Phone number: ")
                email = self.get_input("Email: ")
                
                if not first_name or not last_name or not email:
                    print("First name, last name, and email are required.")
                    continue

                try:
                    zip_code = int(zip_code)
                    phone_number = int(phone_number)
                except ValueError:
                    print("Invalid zip code or phone number. They must be integers.")
                    continue
                
                contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
                self.add_contact(contact)
                
            elif choice == '2':
                print("\nUpdate a contact")
                self.update_person()
                
            elif choice == '3':
                print("\nDelete a contact")
                self.delete_contact()
                
            elif choice == '4':
                print("\nAdd multiple contacts")
                self.add_multiple_contacts()
                
            elif choice == '5':
                print("Exiting the Address Book.")
                break
                
            else:
                print("Invalid choice. Please select a valid option.")

class AddressBookManager:
    def __init__(self):
        self.address_books = {}
    
    def add_address_book(self, name):
        if name in self.address_books:
            print(f"Address book '{name}' already exists.")
        else:
            self.address_books[name] = AddressBook(name)
            print(f"Address book '{name}' added successfully.")
    
    def select_address_book(self):
        print("\nAvailable Address Books:")
        for name in self.address_books.keys():
            print(name)
        name = AddressBook.get_input("Enter the name of the address book you want to use: ")
        if name in self.address_books:
            return self.address_books[name]
        else:
            print(f"No address book found with the name '{name}'.")
            return None

    def search_by_city(self, city):
        results = []
        for address_book in self.address_books.values():
            for contact in address_book.contacts.values():
                for person in contact.values():
                    if person.city.lower() == city.lower():
                        results.append(person)
        return results

    def search_by_state(self, state):
        results = []
        for address_book in self.address_books.values():
            for contact in address_book.contacts.values():
                for person in contact.values():
                    if person.state.lower() == state.lower():
                        results.append(person)
        return results
    
def main():
    manager = AddressBookManager()
    
    while True:
        print("\nMain Menu:")
        print("1. Add an Address Book")
        print("2. Select an Address Book")
        print("3. Search Contacts by City")
        print("4. Search Contacts by State")
        print("5. Exit")

        choice = AddressBook.get_input("Enter your choice: ").strip()

        if choice == '1':
            name = AddressBook.get_input("Enter the name for the new address book: ")
            manager.add_address_book(name)

        elif choice == '2':
            address_book = manager.select_address_book()
            if address_book:
                address_book.run()

        elif choice == '3':
            city = AddressBook.get_input("Enter city to search for: ")
            results = manager.search_by_city(city)
            if results:
                print(f"\nContacts in city '{city}':")
                for contact in results:
                    print(contact)
            else:
                print(f"No contacts found in city '{city}'.")

        elif choice == '4':
            state = AddressBook.get_input("Enter state to search for: ")
            results = manager.search_by_state(state)
            if results:
                print(f"\nContacts in state '{state}':")
                for contact in results:
                    print(contact)
            else:
                print(f"No contacts found in state '{state}'.")

        elif choice == '5':
            print("Exiting the Address Book Manager.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
