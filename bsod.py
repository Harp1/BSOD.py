from tkinter import *
import time

bsod = Tk()
bsod.state("zoomed")
bsod.configure(bg="#0262AF")
bsod.wm_attributes("-toolwindow", 1)

bsodfrown = Label(bsod, text=":( Your PC is boiling mad!", bg="#0262AF", fg="white", font=("consolas", 40))
bsodfrown.pack(pady=20)

bsoddetails = Label(bsod, text="Oh, no! Your PC is boiling mad. This software is trying to calm it down by using a stack of big ice cubes. Please wait for this process to complete.", bg="#0262AF", fg="white", font=("classic console neue", 30), wraplength=800)
bsoddetails.pack(pady=20)

bsodspinner = Label(bsod, text="Loading...\n", bg="#0262AF", fg="white", font=("consolas", 40))
bsodspinner.pack(pady=20)

spinner = ["|", "/", "-", "\"]
i = 0

def update_spinner():
global i
bsodspinner.configure(text="Loading... " + spinner[i % len(spinner)])
i += 1
bsod.after(100, update_spinner)

update_spinner()

bsod.after(5000,bsod.destroy)

bsod.mainloop()
