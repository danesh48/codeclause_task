from tkinter import *
from PIL import ImageTk,Image
import datetime
import time
import winsound



def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        #print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.title("DataFlair Alarm Clock")
clock.iconbitmap(r"alarm_clock.ico")
clock.geometry("400x200")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="yellow",font="arial").place(x=90,y=143)
addTime = Label(clock,text = "Hour  Min     Sec",font=40).place(x = 130)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",font=("Helevetica",8,"bold")).place(x=0, y=31)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=130,y=32)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=170,y=32)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=220,y=32)

img1= Image.open("alarm_clock.png")
rm1 = img1.resize((85, 75))
img11 = ImageTk.PhotoImage(rm1)
l1 = Label(image=img11)
l1.image = img1
l1.place(x=175,y=57)

if hourTime==" " or minTime==" " or secTime==" ":
    Label(clock,text="Enter the correct timing", fg="red").place(x=130,y=37)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10 ,relief = "solid",command = actual_time).place(x =179,y=87)

clock.mainloop()
#Execution of the window.