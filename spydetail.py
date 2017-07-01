from datetime import datetime
class Spy:
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me
spy =Spy('bond','Mr',24,4.7)
friend1=Spy('jyoti','ms','21','4')
friend2=Spy('sudiksh','ms','21','5')
friend3=Spy('sudiksha','komal','22','6')
friends=(friend1,friend2,friend3)