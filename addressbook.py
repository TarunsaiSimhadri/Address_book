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
        self.emial = email
    
class Address:
    def __init__(self):
        self.contacts = {}
        
    
    
