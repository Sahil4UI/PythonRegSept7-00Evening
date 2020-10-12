from datetime import datetime
import calendar
chat =True
while (chat==True):
    message = input("Enter Message")
    message = message.lower()
    helloIntent = ["hello","hi","hie","hey bro","hi bro","wassup buddy"]
    dateIntent = ["show me the current date","current date","date"]
    timeIntent=["current time","time"]

    if message in helloIntent:
        print("Hello Sir...")

    elif message == "bye":
        print("Good bye..TTYL")
        chat = False
        
    elif message in dateIntent:
        currentDate=datetime.now().date()
        print(currentDate.strftime("%d/%m/%y,%a"))

    elif message in timeIntent:
        currentDate=datetime.now().time()
        print(currentDate.strftime("%l-%M-%S,%p"))
        
    elif message =="dayname":
        date=input("Enter Date")
        weekIndex=datetime.strptime(date,"%d %m %Y").weekday()
        print(calendar.day_name[weekIndex])

    else:
        print("Sorry I dont Understand")

        
        
