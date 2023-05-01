from user_Input import *

from Message import Message

array = []

array.append(Message("2025 10 10", "1"))
array.append( Message("2100 6 25", "2"))

for i in array:
    print(i.getRecieve(), i.getMessage())