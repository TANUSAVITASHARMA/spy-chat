from function1 import send_message
from function1 import read_message
from function1 import read_chat_history
from function1 import add_status,start_chat,add_friend
from colorama import Style,Fore,init
from spydetail import Spy,spy,ChatMessage,friends
print "Hello! Let\'s get started"
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question)
if (existing == "Y"):
    start_chat(spy)
else:
     spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
     if len(spy_name) > 0:
        spysalutation = raw_input("Should I call you Mr. or Ms.?: ")
        spy_age = raw_input("What is your age?")
        spy_age = int(spy_age)
        spy_rating = raw_input("What is your spy rating?")
        spy_rating = float(spy_rating)
        spy_is_online=True
        print ("you are added correct information")
        if spy_age > 12 and spy_age < 50:
            print "Authontication complete.welcome "+spy_name+"age:"+str(spy_age)+"and rating of:"+str(spy_rating)+"proud to have you onboard"
     else:
       print 'Please add a valid spy name'
