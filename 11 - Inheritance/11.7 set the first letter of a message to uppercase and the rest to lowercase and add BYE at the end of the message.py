import SMS as sms
import Email as email

class Message():
    def __init__(self):
        self.message = ''
#     def set_message(self, message):
#         arrayson = message.split()
#         
#         for i in range(len(arrayson)):
#             arrayson[i] = arrayson[i].lower()
#         
#         arrayson[0] = arrayson[0].upper()
#         arrayson.append("BYE.")  
#         
#         textson = " ".join(arrayson)
    def set_message(self, message):
        self.message = message.lower()
        self.message = message.capitalize()

mesa = Message()
mesa.set_message("I would like to inform you that our Thursday meeting has been canceled.")

essemess = sms.SMS("111 333 222","888 999 777")
essemess.send(mesa.message)

print()

eemayl = email.Email("sendson@jeezman.com","recipison@yikes.com","Regarding the Thursday meeting")
eemayl.send(mesa.message)