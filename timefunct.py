from tkinter import *
import time

# Window Setup
root = Tk()
# Timer Variables
time_sec = StringVar()
sec = 0

# Timer Start
def start():
    while 1:
        time.sleep(10)
        sec = sec + 10
        time_sec.set(sec)
        start()

# Timer Setup
Button(root,
       fg='blue',
       text='Start',
       command=start).pack()

# Program Loop
root.mainloop()