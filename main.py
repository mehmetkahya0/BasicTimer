# Updated Basic_Timer V2
# update date = 21.04.2023
# Update Notes: i added some messages and i added remaning time.

import tkinter as tk
from tkinter import ttk, messagebox
import time
import chime

class TimerGUI:

    def __init__(self, master):
        self.master = master   
        master.title("Timer")
        master.geometry("400x200")
        master.resizable(width=False, height=False)
        master.configure(bg='white')
        
        # Create style for ttk widgets
        self.style = ttk.Style()
        self.style.configure("Custom.TLabel", font=("'Open Sans', Courier, monospace", 10), background="white")
        self.style.configure("Custom.TEntry", font=("'Courier New', Courier, monospace", 10), background="white")
        
        # Create input variables
        self.minutes = tk.IntVar()
        self.seconds = tk.IntVar()
        
        # Create input fields
        ttk.Label(master, text="Minute: ", style="Custom.TLabel").place(x=10, y=20)
        ttk.Entry(master, width=5, textvariable=self.minutes, style="Custom.TEntry").place(x=55, y=20)
        ttk.Label(master, text="Seconds: ", style="Custom.TLabel").place(x=10, y=50)
        ttk.Entry(master, width=5, textvariable=self.seconds, style="Custom.TEntry").place(x=55, y=50)
        
        # Create start button
        ttk.Button(master, text="Start", command=self.start_timer, width=15).place(x=60, y=80)
        
        # Create progress bar
        self.progress = ttk.Progressbar(master, orient="horizontal", length=300, mode="determinate")
        self.progress.place(x=50, y=120)
           
        # Display creator name
        ttk.Label(master, text="Mehmet Kahya", font=("Calibri", 10), background="#18191A").place(x=150, y=170)
        
        self.timer_running = False
    
    def start_timer(self):
        if self.timer_running:
            return
        
        # Validate input
        minutes = self.minutes.get()
        seconds = self.seconds.get()
        if minutes <= 0 and seconds <= 0:
            messagebox.showerror("Input Error", "Please enter a positive number of minutes or seconds")
            return
        elif seconds < 0 or seconds >= 60:
            messagebox.showerror("Input Error", "Please enter a valid number of seconds (0-59)")
            return
        
        # Set timer variables
        self.remaining_time = minutes * 60 + seconds
        self.progress["maximum"] = self.remaining_time
        self.progress["value"] = self.remaining_time
        self.progress.update()
        self.timer_running = True
        
        # Start timer
        self.start_time = time.monotonic()
        self.update_timer()
        
    def update_timer(self):
        if not self.timer_running:
            return
        
        # Calculate remaining time
        elapsed_time = time.monotonic() - self.start_time
        remaining_time = self.remaining_time - int(elapsed_time)
        
        if remaining_time <= 0:
            self.timer_running = False
            self.progress["value"] = 0
            self.progress.update()
            self.message.configure(text="Timer expired!")
            self.play_sound()
            messagebox.showwarning("Timer", "Time's up!")  # Uyarı mesajı göster

            return
        
        # Update progress bar and remaining time label
        self.progress["value"] = remaining_time
        self.progress.update()
        self.message.configure(text="{} seconds remaining".format(remaining_time))
        
        # Schedule next update
        self.master.after(1000, self.update_timer)
    
    def play_sound(self):
        # Play sound using chime library
        with chime.TemporaryMute():
            chime.theme('zelda')
            chime.error()
    
root = tk.Tk()
root.configure(bg='#18191A')
gui = TimerGUI(root)

root.mainloop()

