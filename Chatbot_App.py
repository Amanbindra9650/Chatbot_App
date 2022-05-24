from datetime import datetime as dt
import os, random

textIntent = ["Hi", "Hello", "Hey"]
dateIntent = ["date", "Hello date"]
timeIntent = ["time", "Hello time"]
musicIntent = ["music", "song", "play song"]

flag = True

while flag:
    msg = input("Enter your message : ")
    if msg in textIntent:
        print("Hello user")
    elif msg in dateIntent:
        date = dt.now().date()
        print("Date is :", date.strftime("%d / %m / %y"))
    elif msg in timeIntent:
        time = dt.now().time()
        print("Date is :", time.strftime("%I / %M / %S"))
    elif msg in musicIntent:
        path = r'C:\Users\Tarun Gupta\Desktop\Songs'
        os.chdir(path)
        songs = os.listdir()
        song = random.choice(songs)
        os.startfile(song)
    elif msg == 'bye':
        print("Bye user")
        flag = False
        break
    else:
        print("I don't understand")




    


    




    

    

    
   
