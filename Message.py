#Message Class
from user_Input import *

class Message:
        def __init__(self, recieve, message):
            self.recieve = recieve
            self.message = message

        def getRecieve(self):return self.recieve
        def getMessage(self):return self.message
              