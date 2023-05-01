from user_Input import *

#Object class for messages

class Message:
        def __init__(self, recieve, message):
            self.recieve = recieve
            self.message = message

        def getRecieve(self):return self.recieve

        def getMessage(self):return self.message