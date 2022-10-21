
#Mehmet Kahya#
#v1
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import time
import math
import chime

window = Tk()

window.title("Timer")
window.geometry("400x200")
window.configure(bg='white')

in_dakika = tk.IntVar()
in_saniye = tk.IntVar()

L3 = Label(window, text="Mehmet Kahya", bg="white",font=("Calibri",10))
L3.place(x=150,y=170)

#Dakika UI
L1 = Label(window, text="Minute: ",font=("Calibri",10,"bold"))
L1.place(x=10,y=20)

E1 = Entry(window, bd =5, textvariable= in_dakika)
E1.place(x=55,y=20)

#Saniye UI
L2 = Label(window, text="Seconds: ",font=("Calibri",10,"bold"))
L2.place(x=10,y=50)

E2 = Entry(window, bd =5, textvariable= in_saniye)
E2.place(x=55,y=50)

def SystemActivate():
    
    dakika = int(E1.get())
    saniye = int(E2.get())
        
    dakika__convert = int(dakika*60)
    dakika_saniye = int(dakika__convert+saniye)

    time.sleep(dakika_saniye)
    print("time is up!")

    chime.theme('zelda')
    chime.error()()

    L3 = Label(window, text="{} second timer expired!".format(dakika_saniye), font="C:/Windows/Fonts/ARLRDBD.TTF")
    L3.place(x=40,y=110)
    
    messagebox.showwarning("showwarning", "Counter is over!")

B = Button(window, text ="Start", command = SystemActivate , width=15, height=1)
B.place(x=60,y=80)

window.mainloop()
