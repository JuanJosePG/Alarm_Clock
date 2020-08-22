from tkinter import *
from tkinter import ttk
import datetime
import time
import winsound

class Aplication():
    def __init__(self):
        # Set the structure of the window
        self.root=Tk()
        self.root.title('Alarm Clock')
        self.root.geometry('500x200')
        self.root.resizable(width=False, height=False)
        self.root.iconphoto(False, PhotoImage(file='F:\Documentos\GitHub\Alarm Clock\Icon\clock.png'))
        
        # Message for the user
        Label(self.root, text='Set the time (24h format) when to wake you up',pady=5,font=('Courier',12,'bold'), padx=40).place(x=250, y=25, anchor=CENTER)
        Label(self.root, text='Hour', pady=2, font=('Courier',10,'bold')).place(x=84, y=65, anchor=CENTER)
        Label(self.root, text='Minute', pady=2, font=('Courier',10,'bold')).place(x=250, y=65, anchor=CENTER)
        Label(self.root, text='Second', pady=2, font=('Courier',10,'bold')).place(x=416, y=65, anchor=CENTER)
        
        # Set the time
            # First of all, we have to initialize the hour, so we need three variables to set
        self.hour=StringVar()
        self.minute=StringVar()
        self.second=StringVar()

            # Then, we have to configure the entry widget to introduce the time
        Entry(self.root, textvariable=self.hour, width=2, font=('Courier',20,'bold')).place(x=84, y=100, height=50, width=50, anchor=CENTER)
        Entry(self.root, textvariable=self.minute, width=2, font=('Courier',20,'bold')).place(x=250, y=100, height=50, width=50, anchor=CENTER)
        Entry(self.root, textvariable=self.second, width=2, font=('Courier',20,'bold')).place(x=416, y=100, height=50, width=50, anchor=CENTER)

        # Buttons
        Button(self.root, text="Set Alarm", font=('Courier',12,'bold'), command=self.set_time).place(x=84, y=165, width=125, anchor=CENTER)
        Button(self.root, text="Stop Music", font=('Courier',12,'bold'), command=self.stop_music).place(x=250, y=165, width=125, anchor=CENTER)
        Button(self.root, text="Exit", font=('Courirer', 12, 'bold'), command=self.root.destroy).place(x=416, y=165, width=100, anchor=CENTER)

        self.root.mainloop()

    def set_time(self):
        timer=f"{self.hour.get()}:{self.minute.get()}:{self.second.get()}"
        self.alarm(timer) 

    def alarm(self,timer):
        current_time=datetime.datetime.now()
        current_date=current_time.strftime("%A, %d/%m/%Y")
        print("The set date is: ", current_date)
        while True:    
            time.sleep(1)
            current_time_2=datetime.datetime.now()
            c_time=current_time_2.strftime("%H:%M:%S")
            print("The set time is: ", c_time)
            if c_time==timer:
                winsound.PlaySound("F:\Documentos\GitHub\Alarm Clock\Sounds\Imperial-March-Star-Wars.wav", winsound.SND_ASYNC)
                break
    
    def stop_music(self):
        winsound.PlaySound(None,winsound.SND_ASYNC)

def main():
    app=Aplication()
    return 0

if __name__=='__main__':
    main()
