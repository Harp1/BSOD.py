PCErrorSim
PCErrorSim is an original, open-source error simulation written in Python.

Source Code...

``import tkinter as tk
import random

root = tk.Tk()
root.state("zoomed")
root.configure(bg="#F44336")
root.wm_attributes("-toolwindow", 1)

error_messages = [
    "Error: System Overload",
    "Error: Hard Drive Failure",
    "Error: Memory Dump",
    "Error: System Crash",
    "Error: Blue Screen of Death"
]

message = random.choice(error_messages)

error_label = tk.Label(root, text=message, bg="#F44336", fg="white", font=("consolas", 40))
error_label.pack(pady=20)

description = tk.Label(root, text="Your PC is facing a critical error. Please wait while we diagnose and fix the issue.", bg="#F44336", fg="white", font=("consolas", 30), wraplength=800)
description.pack(pady=20)

root.after(5000,root.destroy)

root.mainloop()``



example...
![image](https://user-images.githubusercontent.com/74505920/215506741-4c6b7b7a-c660-4f92-a8e9-dae127ceff94.png)

