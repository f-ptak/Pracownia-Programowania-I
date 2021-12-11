class Contact_List():
    import contact
    def __init__(self):
        self.contactlist = []
    
    def add_contact(self,name,email,telephone):
        new_contact = self.contact.Contact(name,email,telephone)
        self.contactlist.append(new_contact)
        
    def disp_contacts(self):
        for i in range(len(self.contactlist)):
            print(f"{self.contactlist[i].__dict__['name']:15}", end="")
            print(f"{self.contactlist[i].__dict__['email']:30}", end="")
            print(f"{self.contactlist[i].__dict__['telephone']}")