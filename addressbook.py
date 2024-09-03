"""

@Author: TarunSai
@Date: 2024-09-03
@Last Modified by: Tarunsai
@Last Modified time: 
@Title : Addressbook.

"""

class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip, ph_no, email):
        self.firstname = first_name
        self.lastname = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.mobile = ph_no
        self.email = email
    
class AddressBook:
    def __init__(self):
        self.contacts = {}
    
    def add_contact(self, contacts):
        key = (contacts.firstname.lower(), contacts.lastname.lower())
        
        if key not in self.contacts:
            self.contacts[key] = {}
        
        if contacts.email in self.contacts[key]:
            print("Contact already exists.")
        else:
            self.contacts[key][contacts.email] = contacts
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
                print(vars(contact))
            
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
                        person.ph_no = new_mobile
                    except ValueError:
                        print("Invalid phone number. Keeping the current value.")
                
                print("Updated details:")
                print(person)
            else:
                print(f"No contact found with the email {email}.")
        else:
            print(f"No person found with the name {name}.")

    def delete_contact(self):
        name = self.get_input("Enter person name to update (format: first_name last_name): ")
        name_parts = name.split()
        if len(name_parts) != 2:
            print("Invalid format. Please enter in 'first_name last_name' format.")
            return

        first_name, last_name = name_parts
        key = (first_name.lower(), last_name.lower())

        if key in self.contacts:
            del self.contacts[key]
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
        
address_book = AddressBook()
contact1 = Contact("tarun", "sai", "maratahalli", "bangalore", "karnataka", "560037", "8659658652", "tarun.sai@example.com")
address_book.add_contact(contact1)