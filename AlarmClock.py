#importing the date and time module 
import datetime
from playsound import playsound

#accept the time am and pm 
hour = int(input("Enter the hour: "))
min = int(input("Enter the minutes: "))
am_pm = input("am/pm: ")

#for a 12 hour clock 
if am_pm=="pm":
    hour = hour + 12

#Check in order to when to ring 
while True: 
    if hour == datetime.datetime.now().hour and min== datetime.datetime.now().min:
        print("Alarm ringing...")
        playsound("punky.mp3")
        break
