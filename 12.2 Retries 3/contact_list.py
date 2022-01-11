class Contact_List():
    import contact
    
    def __init__(self):
        self.contacts = []
    
    def add(self, name, email, telephone):
        newcontact = self.contact.Contact(name, email, telephone)
        self.contacts.append(newcontact)
    
    def display(self):
        for cont in self.contacts:
            print(f"{cont.__dict__['name']:20}", end="")
            print(f"{cont.__dict__['email']:25}", end="")
            print(f"{cont.__dict__['telephone']}")