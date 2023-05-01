from user_Input import *

#Handles file read and writes
#Main storage for messages

def verifyFile():

    try:
        f = open("secret_messages.txt", "r+")

    except FileNotFoundError as e:
        print("ERROR: FILE NOT FOUND")
        print("Please import a 'secret_messages' text file")
        print("Would you like to create a new 'secret_messages' text file?")
        if yesNo():
            print("Successfully created 'secret_messages'")
            f = open("secret_messages.txt", "w")
            verifyFile()
        else:
            verifyFile()

    f = open("secret_messages.txt", "r+")
    
    f.write("hi")
    for i in f:
        print(i)

verifyFile()

        
