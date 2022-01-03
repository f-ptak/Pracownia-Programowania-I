class Email():
    def __init__(self, sender, recipient, subject):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
    
    def send(self, message):
        self.message = message
        print("Sending Email...")
        print(f"{'From:':8}", self.sender)
        print(f"{'To:':8}", self.recipient)
        print(f"{'Subject:':8}", self.subject)
        print(self.message)