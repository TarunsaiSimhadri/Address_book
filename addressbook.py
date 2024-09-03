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

address_book = AddressBook()
contact1 = Contact("tarun", "sai", "maratahalli", "bangalore", "karnataka", "560037", "8659658652", "tarun.sai@example.com")
address_book.add_contact(contact1)
