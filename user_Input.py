from datetime import datetime

date_format = "%Y %m %d"

#input from user for date to send
def sendDate():
    send_date = input("Enter Send Date (YYYY MM DD): ")
    #invalid input
    try:
        dateObject = datetime.strptime(send_date, date_format)
        # TODO: remove
        print(dateObject)
    except ValueError:
        print("Incorrect date format, should be YYYY MM DD")
        sendDate()
    
    #past date
    if datetime.now() > datetime.strptime(send_date, date_format):
        print("Date has already past")
        sendDate()
        
    return send_date

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
        print("Date has already past")
        recieveDate()

    return recieve_date

def message():
    text = input("Message: ")
    return text

