class SMS():
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient
    
    def send(self, message):
        self.message = message
        print("Sending SMS...")
        print(f"{'From:':5}", self.sender)
        print(f"{'To:':5}", self.recipient)
        print(self.message)