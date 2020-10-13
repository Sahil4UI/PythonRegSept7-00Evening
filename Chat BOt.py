from datetime import datetime
import calendar
import webbrowser
import os,glob
chat =True
while (chat==True):
    message = input("Enter Message")
    message = message.lower()
    helloIntent = ["hello","hi","hie","hey bro","hi bro","wassup buddy"]
    dateIntent = ["show me the current date","current date","date"]
    timeIntent=["current time","time"]
    musicIntent = ["music","play music","song","play song"]

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

    elif message.startswith("open"):
        message = message.split()
        webbrowser.open("https://"+message[-1]+".com")

    elif message in musicIntent:
        path='/Users/brainmentors/Downloads'
        os.chdir(path)
        '''
        pathList=os.listdir()
        for data in pathList:
            print(data)
        '''
        file=glob.glob('*.mp3')
        i=0
        for data in file:
            print(f"{i+1}. {data}")
            i+=1
        choice = int(input("enter music number you wanna play"))
        print("***************************")
        os.startfile(file[choice-1])from datetime import datetime
import calendar
import webbrowser
import os,glob
chat =True
while (chat==True):
    message = input("Enter Message")
    message = message.lower()
    helloIntent = ["hello","hi","hie","hey bro","hi bro","wassup buddy"]
    dateIntent = ["show me the current date","current date","date"]
    timeIntent=["current time","time"]
    musicIntent = ["music","play music","song","play song"]

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

    elif message.startswith("open"):
        message = message.split()
        webbrowser.open("https://"+message[-1]+".com")

    elif message in musicIntent:
        path='/Users/brainmentors/Downloads'
        os.chdir(path)
        '''
        pathList=os.listdir()
        for data in pathList:
            print(data)
        '''
        file=glob.glob('*.mp3')
        i=0
        for data in file:
            print(f"{i+1}. {data}")
            i+=1
        choice = int(input("enter music number you wanna play"))
        print("***************************")
        os.startfile(file[choice-1])
        #*-all
        
        #chdir->change directory
        
        

    else:
        print("Sorry I dont Understand")

        
        
from datetime import datetime
import calendar
import webbrowser
import os,glob
chat =True
while (chat==True):
    message = input("Enter Message")
    message = message.lower()
    helloIntent = ["hello","hi","hie","hey bro","hi bro","wassup buddy"]
    dateIntent = ["show me the current date","current date","date"]
    timeIntent=["current time","time"]
    musicIntent = ["music","play music","song","play song"]

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

    elif message.startswith("open"):
        message = message.split()
        webbrowser.open("https://"+message[-1]+".com")

    elif message in musicIntent:
        path='/Users/brainmentors/Downloads'
        os.chdir(path)
        '''
        pathList=os.listdir()
        for data in pathList:
            print(data)
        '''
        file=glob.glob('*.mp3')
        i=0
        for data in file:
            print(f"{i+1}. {data}")
            i+=1
        choice = int(input("enter music number you wanna play"))
        print("***************************")
        os.startfile(file[choice-1])
        #*-all
        
        #chdir->change directory
        
        

    else:
        print("Sorry I dont Understand")

        
        

        #*-all
        
        #chdir->change directory
        
        

    else:
        print("Sorry I dont Understand")

        
        
from datetime import datetime
import calendar
import webbrowser
import os,glob
chat =True
while (chat==True):
    message = input("Enter Message")
    message = message.lower()
    helloIntent = ["hello","hi","hie","hey bro","hi bro","wassup buddy"]
    dateIntent = ["show me the current date","current date","date"]
    timeIntent=["current time","time"]
    musicIntent = ["music","play music","song","play song"]

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

    elif message.startswith("open"):
        message = message.split()
        webbrowser.open("https://"+message[-1]+".com")

    elif message in musicIntent:
        path='/Users/brainmentors/Downloads'
        os.chdir(path)
        '''
        pathList=os.listdir()
        for data in pathList:
            print(data)
        '''
        file=glob.glob('*.mp3')
        i=0
        for data in file:
            print(f"{i+1}. {data}")
            i+=1
        choice = int(input("enter music number you wanna play"))
        print("***************************")
        os.startfile(file[choice-1])
        #*-all
        
        #chdir->change directory
        
        

    else:
        print("Sorry I dont Understand")

        
        
from datetime import datetime
import calendar
import webbrowser
import os,glob
chat =True
while (chat==True):
    message = input("Enter Message")
    message = message.lower()
    helloIntent = ["hello","hi","hie","hey bro","hi bro","wassup buddy"]
    dateIntent = ["show me the current date","current date","date"]
    timeIntent=["current time","time"]
    musicIntent = ["music","play music","song","play song"]

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

    elif message.startswith("open"):
        message = message.split()
        webbrowser.open("https://"+message[-1]+".com")

    elif message in musicIntent:
        path='/Users/brainmentors/Downloads'
        os.chdir(path)
        '''
        pathList=os.listdir()
        for data in pathList:
            print(data)
        '''
        file=glob.glob('*.mp3')
        i=0
        for data in file:
            print(f"{i+1}. {data}")
            i+=1
        choice = int(input("enter music number you wanna play"))
        print("***************************")
        os.startfile(file[choice-1])
        #*-all
        
        #chdir->change directory
        
        

    else:
        print("Sorry I dont Understand")

        
        
