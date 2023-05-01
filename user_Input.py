from datetime import datetime

date_format = "%Y %m %d"

#input from user for date to recieve
def recieveDate():
    recieve_date = input("Enter Recieve Date (YYYY MM DD): ")
    #invalid input
    try:
        dateObject = datetime.strptime(recieve_date, date_format)
        # TODO: remove
        print(dateObject)
    except ValueError:
        print("Incorrect recieve date format, should be YYYY MM DD")
        recieveDate()
    
    if datetime.now() > datetime.strptime(recieve_date, date_format):
        print("Date has already passed")
        recieveDate()

    return recieve_date

def messageInput():
    text = input("Message: ")
    return text

