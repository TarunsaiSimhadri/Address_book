"""

@Author: TarunSai
@Date: 2024-09-03
@Last Modified by: Tarunsai
@Last Modified time: 
@Title : Addressbook.

"""

import csv
import json

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

    def display_contacts_sorted(self):
        all_contacts = []
        for contacts in self.contacts.values():
            for contact in contacts.values():
                all_contacts.append(contact)
        
        sorted_contacts = sorted(all_contacts, key=lambda x: (x.firstname.lower(), x.lastname.lower()))
        
        print("\nSorted Contacts:")
        for contact in sorted_contacts:
            print(contact)

    def display_contacts_sorted_by_city(self):
        all_contacts = []
        for contacts in self.contacts.values():
            for contact in contacts.values():
                all_contacts.append(contact)
        
        sorted_contacts = sorted(all_contacts, key=lambda x: x.city.lower())
        
        print("\nSorted Contacts by City:")
        for contact in sorted_contacts:
            print(contact)

    def display_contacts_sorted_by_state(self):
        all_contacts = []
        for contacts in self.contacts.values():
            for contact in contacts.values():
                all_contacts.append(contact)
        
        sorted_contacts = sorted(all_contacts, key=lambda x: x.state.lower())
        
        print("\nSorted Contacts by State:")
        for contact in sorted_contacts:
            print(contact)

    def display_contacts_sorted_by_zip(self):
        all_contacts = []
        for contacts in self.contacts.values():
            for contact in contacts.values():
                all_contacts.append(contact)
        
        sorted_contacts = sorted(all_contacts, key=lambda x: x.zip_code)
        
        print("\nSorted Contacts by Zip Code:")
        for contact in sorted_contacts:
            print(contact)

    def write_to_file(self, filename):
        with open(filename, 'w') as file:
            for contacts in self.contacts.values():
                for contact in contacts.values():
                    file.write(f"{contact.firstname},{contact.lastname},{contact.address},{contact.city},{contact.state},{contact.zip_code},{contact.mobile},{contact.email}\n")
        print(f"Address book saved to {filename}.")

    def read_from_file(self, filename):
        self.contacts.clear()  # Clear existing contacts
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 8:
                    first_name, last_name, address, city, state, zip_code, phone_number, email = parts
                    try:
                        zip_code = int(zip_code)
                        phone_number = int(phone_number)
                    except ValueError:
                        print(f"Invalid zip code or phone number in file for email {email}. Skipping this line.")
                        continue
                    
                    contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
                    self.add_contact(contact)
        print(f"Address book loaded from {filename}.")

    def write_to_csv_file(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['First Name', 'Last Name', 'Address', 'City', 'State', 'Zip Code', 'Phone Number', 'Email'])
            for contacts in self.contacts.values():
                for contact in contacts.values():
                    writer.writerow([contact.firstname, contact.lastname, contact.address, contact.city, contact.state, contact.zip_code, contact.mobile, contact.email])
        print(f"Address book saved to {filename}.")

    def read_from_csv_file(self, filename):
        self.contacts.clear()  # Clear existing contacts
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                first_name, last_name, address, city, state, zip_code, phone_number, email = row
                contact = Contact(first_name, last_name, address, city, state, int(zip_code), phone_number, email)
                self.add_contact(contact)
        print(f"Address book loaded from {filename}.")

    def write_to_json(self, filename):
        data = {}
        for contacts in self.contacts.values():
            for contact in contacts.values():
                data[contact.email] = {
                    'first_name': contact.firstname,
                    'last_name': contact.lastname,
                    'address': contact.address,
                    'city': contact.city,
                    'state': contact.state,
                    'zip_code': contact.zip_code,
                    'phone_number': contact.mobile,
                    'email': contact.email
                }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Address book saved to {filename}.")

    def read_from_json(self, filename):
        self.contacts.clear()  # Clear existing contacts
        with open(filename, 'r') as file:
            data = json.load(file)
            for email, contact_info in data.items():
                contact = Contact(
                    contact_info['first_name'],
                    contact_info['last_name'],
                    contact_info['address'],
                    contact_info['city'],
                    contact_info['state'],
                    contact_info['zip_code'],
                    contact_info['phone_number'],
                    email
                )
                self.add_contact(contact)
        print(f"Address book loaded from {filename}.")

    def display_menu(self):
        print("\nAddress Book Menu:")
        print("1. Add a contact")
        print("2. Update a contact")
        print("3. Delete a contact")
        print("4. Add multiple contacts")
        print("5. Display sorted contacts")
        print("6. Display sorted contacts by city")
        print("7. Display sorted contacts by state")
        print("8. Display sorted contacts by zip code")
        print("9. Save address book to file")
        print("10. Load address book from file")
        print("11. Save address book to csv file")
        print("12. Load address book from csv file")
        print("13. Save address book to JSON file")
        print("14. Load address book from JSON file")
        print("15. Exit")

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
                print("\nDisplay sorted contacts")
                self.display_contacts_sorted()
                
            elif choice == '6':
                print("\nDisplay sorted contacts by city")
                self.display_contacts_sorted_by_city()
                
            elif choice == '7':
                print("\nDisplay sorted contacts by state")
                self.display_contacts_sorted_by_state()
                
            elif choice == '8':
                print("\nDisplay sorted contacts by zip code")
                self.display_contacts_sorted_by_zip()

            elif choice == '9':
                filename = self.get_input("Enter filename to save the address book: ")
                self.write_to_file(filename)

            elif choice == '10':
                filename = self.get_input("Enter filename to load the address book: ")
                self.read_from_file(filename)

            elif choice == '11':
                filename = self.get_input("Enter filename to save the address book: ")
                self.write_to_csv_file(filename)
                
            elif choice == '12':
                filename = self.get_input("Enter filename to load the address book: ")
                self.read_from_csv_file(filename)

            elif choice == '13':
                filename = self.get_input("Enter the filename to save the address book as JSON: ")
                self.write_to_json(filename)
                
            elif choice == '14':
                filename = self.get_input("Enter the filename to load the address book from JSON: ")
                self.read_from_json(filename)

            elif choice == '15':
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
    
    def search_by_city(self, city):
        count = 0 
        results = []
        for address_book in self.address_books.values():
            for contact in address_book.contacts.values():
                for person in contact.values():
                    if person.city.lower() == city.lower():
                        count+=1
        return count

    def search_by_state(self, state):
        count  = 0
        results = []
        for address_book in self.address_books.values():
            for contact in address_book.contacts.values():
                for person in contact.values():
                    if person.state.lower() == state.lower():
                        count+=1
        return count
    
def main():
    manager = AddressBookManager()
    
    while True:
        print("\nMain Menu:")
        print("1. Add an Address Book")
        print("2. Select an Address Book")
        print("3. Search Contacts by City")
        print("4. Search Contacts by State")
        print("5. Count Contacts by City")
        print("6. Count Contacts by State")
        print("7. Exit")

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
            city = AddressBook.get_input("Enter city to count contacts for: ")
            count = manager.search_by_city(city)
            print(f"Number of contacts in city '{city}': {count}")

        elif choice == '6':
            state = AddressBook.get_input("Enter state to count contacts for: ")
            count = manager.search_by_state(state)
            print(f"Number of contacts in state '{state}': {count}")

        elif choice == '7':
            print("Exiting the Address Book Manager.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
